#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import urllib.request
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.model import global_efficiency, project_hyperedges
MANIFEST_PATH = ROOT / "data/source_manifest.json"
CURVE_PATH = ROOT / "data/derived/primary_results.csv"
SUMMARY_PATH = ROOT / "results/empirical_summary.json"

REMOVAL_LEVELS = [5, 10, 15, 20, 30]
RANDOM_DRAWS = 200
SEED = 20260925


def fetch_source():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    request = urllib.request.Request(
        manifest["direct_data_url"],
        headers={"User-Agent": "organizational-network-resilience/1.1"},
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        payload = response.read()

    actual_md5 = hashlib.md5(payload).hexdigest()
    expected_md5 = manifest["source_file_md5"]

    if actual_md5 != expected_md5:
        raise RuntimeError(
            f"Source checksum mismatch: expected {expected_md5}, got {actual_md5}. "
            "Stop rather than silently analyzing a different dataset version."
        )

    return json.loads(payload), actual_md5


def deterministic_sample(node_ids, k, draw_index):
    """Select a version-stable pseudo-random subset using SHA-256 ranking."""
    ranked = sorted(
        node_ids,
        key=lambda node: hashlib.sha256(
            f"{SEED}|{k}|{draw_index}|{node}".encode("utf-8")
        ).digest(),
    )
    return ranked[:k]


def analyze(data):
    ids = [str(item["node"]) for item in data["nodes"]]

    by_edge = {}
    for incidence in data["incidences"]:
        by_edge.setdefault(str(incidence["edge"]), []).append(
            str(incidence["node"])
        )

    adjacency = project_hyperedges(ids, by_edge.values())

    # Stable sorting preserves source node order for equal-degree ties.
    degree_ranking = sorted(
        ids,
        key=lambda node: len(adjacency[node]),
        reverse=True,
    )

    baseline_efficiency = global_efficiency(ids, adjacency)
    curve = []

    for k in REMOVAL_LEVELS:
        targeted_retained = (
            global_efficiency(ids, adjacency, set(degree_ranking[:k]))
            / baseline_efficiency
        )

        random_values = sorted(
            global_efficiency(
                ids,
                adjacency,
                set(deterministic_sample(ids, k, draw_index)),
            )
            / baseline_efficiency
            for draw_index in range(RANDOM_DRAWS)
        )

        random_mean = sum(random_values) / len(random_values)

        # Empirical order-statistic diagnostics for 200 draws.
        random_p05 = random_values[9]
        random_p95 = random_values[189]

        curve.append(
            {
                "removed": k,
                "removal_fraction": k / len(ids),
                "targeted_retained_efficiency": targeted_retained,
                "targeted_loss_from_baseline_ratio": 1.0 - targeted_retained,
                "random_mean": random_mean,
                "random_mean_loss_from_baseline_ratio": 1.0 - random_mean,
                "random_p05": random_p05,
                "random_p95": random_p95,
                "gap_vs_random_mean": random_mean - targeted_retained,
                "gap_vs_random_p05": random_p05 - targeted_retained,
                "targeted_below_random_p05": targeted_retained < random_p05,
            }
        )

    k5 = curve[0]
    k30 = curve[-1]

    summary = {
        "study": "Organizational Communication Resilience Under Key-Actor Loss",
        "headline_metrics": {
            "nodes": len(ids),
            "hyperedges": len(data["edges"]),
            "incidences": len(data["incidences"]),
            "projection_edges": sum(len(v) for v in adjacency.values()) // 2,
            "baseline_global_efficiency": round(baseline_efficiency, 4),
            "targeted_retained_efficiency_k30": round(
                k30["targeted_retained_efficiency"], 4
            ),
            "targeted_loss_from_baseline_ratio_k30": round(
                k30["targeted_loss_from_baseline_ratio"], 4
            ),
            "random_retained_efficiency_k30": round(k30["random_mean"], 4),
            "random_mean_loss_from_baseline_ratio_k30": round(
                k30["random_mean_loss_from_baseline_ratio"], 4
            ),
            "removal_fraction_k30": round(k30["removal_fraction"], 4),
        },
        "random_comparator_draws": RANDOM_DRAWS,
        "seed": SEED,
        "random_comparator_method": "SHA-256 rank sampling by seed, removal level, draw index, and node ID",
        "robustness_diagnostics": {
            "targeted_curve_strictly_decreases": all(
                curve[i]["targeted_retained_efficiency"]
                > curve[i + 1]["targeted_retained_efficiency"]
                for i in range(len(curve) - 1)
            ),
            "targeted_below_random_mean_at_all_levels": all(
                item["targeted_retained_efficiency"] < item["random_mean"]
                for item in curve
            ),
            "targeted_below_random_p05_at_all_levels": all(
                item["targeted_below_random_p05"] for item in curve
            ),
            "targeted_random_gap_strictly_widens": all(
                curve[i]["gap_vs_random_mean"]
                < curve[i + 1]["gap_vs_random_mean"]
                for i in range(len(curve) - 1)
            ),
            "gap_vs_random_mean_k5": round(k5["gap_vs_random_mean"], 4),
            "gap_vs_random_mean_k30": round(k30["gap_vs_random_mean"], 4),
            "gap_growth_k5_to_k30": round(
                k30["gap_vs_random_mean"] - k5["gap_vs_random_mean"], 4
            ),
        },
        "finding": (
            "Static degree-targeted actor loss reduces retained global efficiency "
            "much more strongly than same-count comparator loss under the released "
            "Enron communication-network projection. At 30 removals, targeted "
            "retained efficiency is 0.8608 versus a comparator mean of 0.9917, and "
            "the targeted result remains below the comparator 5th-percentile "
            "order-statistic bound."
        ),
        "source": "email-enron temporal hypergraph (XGI / Zenodo), version v0.1",
        "retrieved": "2026-09-25",
        "release_version": "1.1.0",
        "interpretation_boundary": (
            "Email connectivity is a proxy for potential structural information "
            "access, not direct evidence of tacit knowledge, expertise, employee "
            "value, learning effectiveness, or causal organizational performance."
        ),
    }

    return summary, curve


def rounded_curve(curve):
    output = []

    for row in curve:
        output.append(
            {
                "removed": row["removed"],
                "removal_fraction": round(row["removal_fraction"], 4),
                "targeted_retained_efficiency": round(
                    row["targeted_retained_efficiency"], 4
                ),
                "targeted_loss_from_baseline_ratio": round(
                    row["targeted_loss_from_baseline_ratio"], 4
                ),
                "random_mean": round(row["random_mean"], 4),
                "random_mean_loss_from_baseline_ratio": round(
                    row["random_mean_loss_from_baseline_ratio"], 4
                ),
                "random_p05": round(row["random_p05"], 4),
                "random_p95": round(row["random_p95"], 4),
                "gap_vs_random_mean": round(row["gap_vs_random_mean"], 4),
                "gap_vs_random_p05": round(row["gap_vs_random_p05"], 4),
                "targeted_below_random_p05": str(
                    row["targeted_below_random_p05"]
                ).lower(),
            }
        )

    return output


def write_outputs(summary, curve):
    rows = rounded_curve(curve)

    CURVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)

    with CURVE_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )


def read_packaged_curve():
    with CURVE_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def check_release(summary, curve):
    expected_rows = rounded_curve(curve)
    packaged_rows = read_packaged_curve()

    if len(expected_rows) != len(packaged_rows):
        raise SystemExit("FAIL: packaged curve row count differs")

    for expected, packaged in zip(expected_rows, packaged_rows):
        for key, value in expected.items():
            if key == "targeted_below_random_p05":
                if str(packaged[key]).lower() != str(value).lower():
                    raise SystemExit(
                        f"FAIL: packaged curve differs at k={expected['removed']} / {key}: "
                        f"{packaged[key]} != {value}"
                    )
            elif key == "removed":
                if int(packaged[key]) != int(value):
                    raise SystemExit(
                        f"FAIL: packaged curve differs at k={expected['removed']} / {key}: "
                        f"{packaged[key]} != {value}"
                    )
            elif abs(float(packaged[key]) - float(value)) > 5e-5:
                raise SystemExit(
                    f"FAIL: packaged curve differs at k={expected['removed']} / {key}: "
                    f"{packaged[key]} != {value}"
                )

    packaged_summary = json.loads(
        SUMMARY_PATH.read_text(encoding="utf-8")
    )
    if packaged_summary != summary:
        raise SystemExit("FAIL: packaged empirical summary differs from source rebuild")

    print("zenodo_rebuild: PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="Regenerate packaged CSV and JSON outputs after checksum verification.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Rebuild from the pinned source and require exact packaged agreement.",
    )
    args = parser.parse_args()

    data, md5 = fetch_source()
    summary, curve = analyze(data)

    if args.write:
        write_outputs(summary, curve)

    rebuilt = {
        "source_md5": md5,
        "summary": summary,
        "curve": rounded_curve(curve),
    }
    print(json.dumps(rebuilt, indent=2))

    if args.check:
        check_release(summary, curve)


if __name__ == "__main__":
    main()
