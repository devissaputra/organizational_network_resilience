#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import urllib.request
from pathlib import Path

from research.model import global_efficiency, project_hyperedges

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data/source_manifest.json"
CURVE_PATH = ROOT / "data/derived/primary_results.csv"
SUMMARY_PATH = ROOT / "results/empirical_summary.json"
REMOVAL_LEVELS = [5, 10, 15, 20, 30]
RANDOM_DRAWS = 200
SEED = 20260925


def fetch_source():
    manifest = json.loads(MANIFEST_PATH.read_text())
    req = urllib.request.Request(
        manifest["direct_data_url"],
        headers={"User-Agent": "organizational-network-resilience/1.0"},
    )
    with urllib.request.urlopen(req) as response:
        payload = response.read()

    actual_md5 = hashlib.md5(payload).hexdigest()
    expected_md5 = manifest["source_file_md5"]
    if actual_md5 != expected_md5:
        raise RuntimeError(
            f"Source checksum mismatch: expected {expected_md5}, got {actual_md5}. "
            "Stop rather than silently analyzing a different dataset version."
        )
    return json.loads(payload), actual_md5


def analyze(d):
    ids = [str(x["node"]) for x in d["nodes"]]
    by_edge = {}
    for incidence in d["incidences"]:
        by_edge.setdefault(str(incidence["edge"]), []).append(str(incidence["node"]))

    adj = project_hyperedges(ids, by_edge.values())

    # Python sorting is stable, so equal-degree ties retain the dataset node order.
    degree = sorted(ids, key=lambda x: len(adj[x]), reverse=True)
    base_eff = global_efficiency(ids, adj)
    rng = random.Random(SEED)
    curve = []

    for k in REMOVAL_LEVELS:
        targeted = global_efficiency(ids, adj, set(degree[:k])) / base_eff
        vals = sorted(
            global_efficiency(ids, adj, set(rng.sample(ids, k))) / base_eff
            for _ in range(RANDOM_DRAWS)
        )
        random_mean = sum(vals) / len(vals)
        p05 = vals[9]
        p95 = vals[189]
        curve.append(
            {
                "removed": k,
                "targeted_retained_efficiency": targeted,
                "random_mean": random_mean,
                "random_p05": p05,
                "random_p95": p95,
                "gap_vs_random_mean": random_mean - targeted,
                "gap_vs_random_p05": p05 - targeted,
                "targeted_below_random_p05": targeted < p05,
            }
        )

    k5 = curve[0]
    k30 = curve[-1]
    summary = {
        "study": "Organizational Communication Resilience Under Key-Actor Loss",
        "headline_metrics": {
            "nodes": len(ids),
            "hyperedges": len(d["edges"]),
            "incidences": len(d["incidences"]),
            "projection_edges": sum(len(v) for v in adj.values()) // 2,
            "baseline_global_efficiency": round(base_eff, 4),
            "targeted_retained_efficiency_k30": round(k30["targeted_retained_efficiency"], 4),
            "random_retained_efficiency_k30": round(k30["random_mean"], 4),
        },
        "random_comparator_draws": RANDOM_DRAWS,
        "seed": SEED,
        "robustness_diagnostics": {
            "targeted_below_random_p05_at_all_levels": all(
                x["targeted_below_random_p05"] for x in curve
            ),
            "gap_vs_random_mean_k5": round(k5["gap_vs_random_mean"], 4),
            "gap_vs_random_mean_k30": round(k30["gap_vs_random_mean"], 4),
            "gap_growth_k5_to_k30": round(
                k30["gap_vs_random_mean"] - k5["gap_vs_random_mean"], 4
            ),
        },
        "finding": (
            "Targeted removal progressively lowers normalized global efficiency while "
            "same-count random removal leaves mean efficiency close to baseline. "
            "At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 "
            "under random removal."
        ),
        "source": "email-enron temporal hypergraph (XGI / Zenodo)",
        "retrieved": "2026-09-25",
    }
    return summary, curve


def rounded_curve(curve):
    rows = []
    for r in curve:
        rows.append(
            {
                "removed": r["removed"],
                "targeted_retained_efficiency": round(r["targeted_retained_efficiency"], 4),
                "random_mean": round(r["random_mean"], 4),
                "random_p05": round(r["random_p05"], 4),
                "random_p95": round(r["random_p95"], 4),
                "gap_vs_random_mean": round(r["gap_vs_random_mean"], 4),
                "gap_vs_random_p05": round(r["gap_vs_random_p05"], 4),
                "targeted_below_random_p05": str(r["targeted_below_random_p05"]).lower(),
            }
        )
    return rows


def write_outputs(summary, curve):
    rows = rounded_curve(curve)
    CURVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(rows[0].keys())
    with CURVE_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="Regenerate the packaged CSV and JSON outputs after checksum verification.",
    )
    args = parser.parse_args()

    data, md5 = fetch_source()
    summary, curve = analyze(data)
    if args.write:
        write_outputs(summary, curve)

    print(
        json.dumps(
            {"source_md5": md5, "summary": summary, "curve": rounded_curve(curve)},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
