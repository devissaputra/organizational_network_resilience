from research.model import (
    EXPECTED_REMOVAL_LEVELS,
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
    adjacency = project_hyperedges(nodes, [["a", "b"], ["b", "c"]])

    assert adjacency["b"] == {"a", "c"}
    assert round(global_efficiency(nodes, adjacency), 4) == 0.8333


def test_disconnected_pairs_contribute_zero():
    nodes = ["a", "b", "c"]
    adjacency = project_hyperedges(nodes, [["a", "b"]])

    assert round(global_efficiency(nodes, adjacency), 4) == 0.3333


def test_removal_can_reduce_efficiency():
    nodes = ["a", "b", "c", "d"]
    adjacency = project_hyperedges(
        nodes,
        [["a", "b"], ["b", "c"], ["c", "d"]],
    )

    assert (
        global_efficiency(nodes, adjacency, {"b"})
        < global_efficiency(nodes, adjacency)
    )


def test_retained_efficiency_can_exceed_one_for_survivors():
    nodes = ["a", "b", "c", "d"]
    adjacency = project_hyperedges(
        nodes,
        [["a", "b"], ["b", "c"], ["c", "a"]],
    )
    baseline = global_efficiency(nodes, adjacency)
    after = global_efficiency(nodes, adjacency, {"d"})

    assert after / baseline > 1.0


def test_release_curve_and_diagnostics():
    rows = load_curve()
    diagnostics = curve_diagnostics(rows)

    assert [int(row["removed"]) for row in rows] == EXPECTED_REMOVAL_LEVELS
    assert diagnostics["removal_levels_match_release"]
    assert diagnostics["removal_fraction_matches_node_count"]
    assert diagnostics["targeted_loss_fields_valid"]
    assert diagnostics["random_loss_fields_valid"]
    assert diagnostics["targeted_curve_strictly_decreases"]
    assert diagnostics["targeted_random_gap_strictly_widens"]
    assert diagnostics["targeted_below_random_mean_at_all_levels"]
    assert diagnostics["targeted_below_random_p05_at_all_levels"]
    assert diagnostics["random_interval_order_valid"]

    assert round(diagnostics["gap_k5"], 4) == 0.0243
    assert round(diagnostics["gap_k30"], 4) == 0.1309
    assert round(diagnostics["gap_growth"], 4) == 0.1066


def test_k30_release_values():
    rows = load_curve()
    summary = load_summary()
    k30 = rows[-1]
    metrics = summary["headline_metrics"]

    assert float(k30["removal_fraction"]) == 0.2027
    assert float(k30["targeted_retained_efficiency"]) == 0.8608
    assert float(k30["targeted_loss_from_baseline_ratio"]) == 0.1392
    assert float(k30["random_mean"]) == 0.9917
    assert float(k30["random_mean_loss_from_baseline_ratio"]) == 0.0083

    assert metrics["targeted_retained_efficiency_k30"] == 0.8608
    assert metrics["targeted_loss_from_baseline_ratio_k30"] == 0.1392
    assert metrics["random_retained_efficiency_k30"] == 0.9917
    assert metrics["random_mean_loss_from_baseline_ratio_k30"] == 0.0083
    assert metrics["removal_fraction_k30"] == 0.2027


def test_source_manifest_pins_dataset_identity():
    manifest = load_manifest()

    assert manifest["dataset_version"] == "v0.1"
    assert manifest["doi"] == "10.5281/zenodo.21909507"
    assert (
        manifest["source_file_md5"]
        == "3666af1fc5a190d93f7fd98cff58e283"
    )
    assert manifest["raw_data_redistributed"] is False


def test_summary_random_design_is_pinned():
    summary = load_summary()

    assert summary["random_comparator_draws"] == 200
    assert summary["seed"] == 20260925
    assert summary["robustness_diagnostics"][
        "targeted_below_random_p05_at_all_levels"
    ] is True


def test_packaged_bundle_validation():
    assert validate_bundle()
