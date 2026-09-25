import json
from pathlib import Path

from research.model import (
    curve_diagnostics,
    global_efficiency,
    load_curve,
    load_manifest,
    load_summary,
    project_hyperedges,
    validate_bundle,
)


def test_projection_and_efficiency():
    nodes = ["a", "b", "c"]
    adj = project_hyperedges(nodes, [["a", "b"], ["b", "c"]])
    assert adj["b"] == {"a", "c"}
    assert round(global_efficiency(nodes, adj), 4) == 0.8333


def test_disconnected_pairs_contribute_zero():
    nodes = ["a", "b", "c"]
    adj = project_hyperedges(nodes, [["a", "b"]])
    assert round(global_efficiency(nodes, adj), 4) == 0.3333


def test_removal_can_reduce_efficiency():
    nodes = ["a", "b", "c", "d"]
    adj = project_hyperedges(nodes, [["a", "b"], ["b", "c"], ["c", "d"]])
    assert global_efficiency(nodes, adj, {"b"}) < global_efficiency(nodes, adj)


def test_release_curve_and_hypothesis_diagnostics():
    rows = load_curve()
    d = curve_diagnostics(rows)
    assert d["removal_levels_match_release"]
    assert d["targeted_curve_strictly_decreases"]
    assert d["targeted_random_gap_strictly_widens"]
    assert d["targeted_below_random_mean_at_all_levels"]
    assert d["targeted_below_random_p05_at_all_levels"]
    assert d["random_interval_order_valid"]
    assert round(d["gap_k5"], 4) == 0.0238
    assert round(d["gap_k30"], 4) == 0.1304


def test_k30_summary_matches_packaged_curve():
    rows = load_curve()
    summary = load_summary()
    k30 = rows[-1]
    metrics = summary["headline_metrics"]
    assert float(k30["targeted_retained_efficiency"]) == metrics["targeted_retained_efficiency_k30"]
    assert float(k30["random_mean"]) == metrics["random_retained_efficiency_k30"]
    assert summary["random_comparator_draws"] == 200


def test_source_manifest_pins_dataset_version_and_checksum():
    manifest = load_manifest()
    assert manifest["dataset_version"] == "v0.1"
    assert manifest["doi"] == "10.5281/zenodo.21909507"
    assert manifest["source_file_md5"] == "3666af1fc5a190d93f7fd98cff58e283"
    assert manifest["raw_data_redistributed"] is False


def test_packaged_bundle_validation():
    assert validate_bundle()
