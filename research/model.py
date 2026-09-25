from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REMOVAL_LEVELS = [5, 10, 15, 20, 30]
EXPECTED_NODE_COUNT = 148
EXPECTED_HYPEREDGE_COUNT = 10885
EXPECTED_INCIDENCE_COUNT = 26914
EXPECTED_PROJECTION_EDGES = 2583
EXPECTED_SOURCE_MD5 = "3666af1fc5a190d93f7fd98cff58e283"
EXPECTED_DOI = "10.5281/zenodo.21909507"
EXPECTED_VERSION = "v0.1"


def project_hyperedges(nodes, hyperedges):
    """Project hyperedges into an undirected simple adjacency mapping."""
    adjacency = {str(node): set() for node in nodes}

    for edge in hyperedges:
        members = list(dict.fromkeys(map(str, edge)))
        for index, u in enumerate(members):
            for v in members[index + 1 :]:
                adjacency[u].add(v)
                adjacency[v].add(u)

    return adjacency


def global_efficiency(nodes, adjacency, removed=frozenset()):
    """Compute global efficiency among surviving nodes."""
    removed = {str(node) for node in removed}
    available = [str(node) for node in nodes if str(node) not in removed]

    if len(available) < 2:
        return 0.0

    total = 0.0
    pairs = 0

    for index, source in enumerate(available):
        distances = {source: 0}
        queue = [source]

        for node in queue:
            for neighbor in adjacency.get(node, ()):
                if neighbor not in removed and neighbor not in distances:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)

        for destination in available[index + 1 :]:
            pairs += 1
            distance = distances.get(destination)
            if distance:
                total += 1.0 / distance

    return total / pairs


def load_curve():
    with (ROOT / "data/derived/primary_results.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        return list(csv.DictReader(handle))


def load_summary():
    return json.loads(
        (ROOT / "results/empirical_summary.json").read_text(encoding="utf-8")
    )


def load_manifest():
    return json.loads(
        (ROOT / "data/source_manifest.json").read_text(encoding="utf-8")
    )


def curve_diagnostics(rows=None):
    rows = rows or load_curve()

    removed = [int(row["removed"]) for row in rows]
    removal_fraction = [float(row["removal_fraction"]) for row in rows]
    targeted = [float(row["targeted_retained_efficiency"]) for row in rows]
    targeted_loss = [
        float(row["targeted_loss_from_baseline_ratio"]) for row in rows
    ]
    random_mean = [float(row["random_mean"]) for row in rows]
    random_loss = [
        float(row["random_mean_loss_from_baseline_ratio"]) for row in rows
    ]
    p05 = [float(row["random_p05"]) for row in rows]
    p95 = [float(row["random_p95"]) for row in rows]
    gaps = [float(row["gap_vs_random_mean"]) for row in rows]

    return {
        "removal_levels_match_release": removed == EXPECTED_REMOVAL_LEVELS,
        "removal_fraction_matches_node_count": all(
            abs(fraction - round(k / EXPECTED_NODE_COUNT, 4)) <= 5e-5
            for k, fraction in zip(removed, removal_fraction)
        ),
        "targeted_loss_fields_valid": all(
            abs(loss - round(1.0 - retained, 4)) <= 5e-5
            for loss, retained in zip(targeted_loss, targeted)
        ),
        "random_loss_fields_valid": all(
            abs(loss - round(1.0 - retained, 4)) <= 5e-5
            for loss, retained in zip(random_loss, random_mean)
        ),
        "targeted_curve_strictly_decreases": all(
            targeted[i] > targeted[i + 1]
            for i in range(len(targeted) - 1)
        ),
        "targeted_random_gap_strictly_widens": all(
            gaps[i] < gaps[i + 1] for i in range(len(gaps) - 1)
        ),
        "targeted_below_random_mean_at_all_levels": all(
            targeted_value < random_value
            for targeted_value, random_value in zip(targeted, random_mean)
        ),
        "targeted_below_random_p05_at_all_levels": all(
            targeted_value < lower
            for targeted_value, lower in zip(targeted, p05)
        ),
        "random_interval_order_valid": all(
            lower <= mean <= upper
            for lower, mean, upper in zip(p05, random_mean, p95)
        ),
        "gap_k5": gaps[0],
        "gap_k30": gaps[-1],
        "gap_growth": gaps[-1] - gaps[0],
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
        "removal_fraction_matches_node_count",
        "targeted_loss_fields_valid",
        "random_loss_fields_valid",
        "targeted_curve_strictly_decreases",
        "targeted_random_gap_strictly_widens",
        "targeted_below_random_mean_at_all_levels",
        "targeted_below_random_p05_at_all_levels",
        "random_interval_order_valid",
    )
    if not all(diagnostics[name] for name in required_checks):
        return False

    metrics = summary.get("headline_metrics", {})
    expected_counts = {
        "nodes": EXPECTED_NODE_COUNT,
        "hyperedges": EXPECTED_HYPEREDGE_COUNT,
        "incidences": EXPECTED_INCIDENCE_COUNT,
        "projection_edges": EXPECTED_PROJECTION_EDGES,
    }
    if any(int(metrics.get(key, -1)) != value for key, value in expected_counts.items()):
        return False

    k30 = rows[-1]
    exact_checks = {
        "targeted_retained_efficiency_k30": k30["targeted_retained_efficiency"],
        "targeted_loss_from_baseline_ratio_k30": k30["targeted_loss_from_baseline_ratio"],
        "random_retained_efficiency_k30": k30["random_mean"],
        "random_mean_loss_from_baseline_ratio_k30": k30["random_mean_loss_from_baseline_ratio"],
        "removal_fraction_k30": k30["removal_fraction"],
    }
    for key, value in exact_checks.items():
        if abs(float(metrics.get(key, -1)) - float(value)) > 5e-5:
            return False

    robustness = summary.get("robustness_diagnostics", {})
    if robustness.get("targeted_curve_strictly_decreases") is not True:
        return False
    if robustness.get("targeted_below_random_mean_at_all_levels") is not True:
        return False
    if robustness.get("targeted_below_random_p05_at_all_levels") is not True:
        return False
    if robustness.get("targeted_random_gap_strictly_widens") is not True:
        return False
    if abs(float(robustness.get("gap_vs_random_mean_k5", -1)) - diagnostics["gap_k5"]) > 5e-5:
        return False
    if abs(float(robustness.get("gap_vs_random_mean_k30", -1)) - diagnostics["gap_k30"]) > 5e-5:
        return False
    if abs(float(robustness.get("gap_growth_k5_to_k30", -1)) - diagnostics["gap_growth"]) > 5e-5:
        return False

    if manifest.get("source_file_md5") != EXPECTED_SOURCE_MD5:
        return False
    if manifest.get("doi") != EXPECTED_DOI:
        return False
    if manifest.get("dataset_version") != EXPECTED_VERSION:
        return False
    if manifest.get("raw_data_redistributed") is not False:
        return False

    if summary.get("random_comparator_draws") != 200:
        return False
    if summary.get("seed") != 20260925:
        return False

    return True
