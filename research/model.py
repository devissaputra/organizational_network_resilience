from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REMOVAL_LEVELS = [5, 10, 15, 20, 30]


def project_hyperedges(nodes, hyperedges):
    """Project hyperedges into an undirected simple adjacency mapping."""
    adj = {str(n): set() for n in nodes}
    for edge in hyperedges:
        ns = list(dict.fromkeys(map(str, edge)))
        for i, u in enumerate(ns):
            for v in ns[i + 1 :]:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def global_efficiency(nodes, adj, removed=frozenset()):
    """Global efficiency among surviving nodes after a removal set."""
    removed = {str(x) for x in removed}
    avail = [str(x) for x in nodes if str(x) not in removed]
    if len(avail) < 2:
        return 0.0

    total = 0.0
    pairs = 0
    for i, src in enumerate(avail):
        dist = {src: 0}
        queue = [src]
        for u in queue:
            for v in adj.get(u, ()):
                if v not in removed and v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        for dst in avail[i + 1 :]:
            pairs += 1
            d = dist.get(dst)
            if d:
                total += 1.0 / d
    return total / pairs


def load_curve():
    with (ROOT / "data/derived/primary_results.csv").open(newline="") as f:
        return list(csv.DictReader(f))


def load_summary():
    return json.loads((ROOT / "results/empirical_summary.json").read_text())


def load_manifest():
    return json.loads((ROOT / "data/source_manifest.json").read_text())


def curve_diagnostics(rows=None):
    rows = rows or load_curve()
    removed = [int(r["removed"]) for r in rows]
    targeted = [float(r["targeted_retained_efficiency"]) for r in rows]
    random_mean = [float(r["random_mean"]) for r in rows]
    p05 = [float(r["random_p05"]) for r in rows]
    p95 = [float(r["random_p95"]) for r in rows]
    gaps = [m - t for m, t in zip(random_mean, targeted)]

    return {
        "removal_levels_match_release": removed == EXPECTED_REMOVAL_LEVELS,
        "targeted_curve_strictly_decreases": all(
            targeted[i] > targeted[i + 1] for i in range(len(targeted) - 1)
        ),
        "targeted_random_gap_strictly_widens": all(
            gaps[i] < gaps[i + 1] for i in range(len(gaps) - 1)
        ),
        "targeted_below_random_mean_at_all_levels": all(
            t < m for t, m in zip(targeted, random_mean)
        ),
        "targeted_below_random_p05_at_all_levels": all(
            t < lo for t, lo in zip(targeted, p05)
        ),
        "random_interval_order_valid": all(
            lo <= m <= hi for lo, m, hi in zip(p05, random_mean, p95)
        ),
        "gap_k5": gaps[0],
        "gap_k30": gaps[-1],
    }


def validate_bundle():
    rows = load_curve()
    summary = load_summary()
    manifest = load_manifest()
    if len(rows) != len(EXPECTED_REMOVAL_LEVELS):
        return False

    diagnostics = curve_diagnostics(rows)
    required_checks = (
        "removal_levels_match_release",
        "targeted_curve_strictly_decreases",
        "targeted_random_gap_strictly_widens",
        "targeted_below_random_mean_at_all_levels",
        "targeted_below_random_p05_at_all_levels",
        "random_interval_order_valid",
    )
    if not all(diagnostics[name] for name in required_checks):
        return False

    k30 = rows[-1]
    metrics = summary.get("headline_metrics", {})
    if abs(float(k30["targeted_retained_efficiency"]) - float(metrics.get("targeted_retained_efficiency_k30", -1))) > 5e-5:
        return False
    if abs(float(k30["random_mean"]) - float(metrics.get("random_retained_efficiency_k30", -1))) > 5e-5:
        return False

    expected_counts = {"nodes": 148, "hyperedges": 10885, "incidences": 26914, "projection_edges": 2583}
    if any(int(metrics.get(k, -1)) != v for k, v in expected_counts.items()):
        return False

    if manifest.get("source_file_md5") != "3666af1fc5a190d93f7fd98cff58e283":
        return False
    if summary.get("random_comparator_draws") != 200:
        return False
    return True
