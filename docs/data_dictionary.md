# Data Dictionary

## Provenance

See `data/source_manifest.json`.

The release pins:

- Zenodo DOI 10.5281/zenodo.21909507;
- dataset version v0.1;
- source file `email-enron.json`;
- source MD5 `3666af1fc5a190d93f7fd98cff58e283`.

Raw source observations are not republished.

## Source structure

The HIF-style JSON contains:

- `nodes`;
- `edges`;
- `incidences`.

The released analysis groups incidences by edge to reconstruct email hyperedge membership.

## `data/derived/primary_results.csv`

Complete five-level resilience stress curve.

Columns:

- `removed`: number of actors removed;
- `removal_fraction`: removed actors divided by 148;
- `targeted_retained_efficiency`: targeted post-removal efficiency divided by intact efficiency;
- `targeted_loss_from_baseline_ratio`: 1 minus targeted retained efficiency;
- `random_mean`: mean retained efficiency across 200 seeded same-count random draws;
- `random_mean_loss_from_baseline_ratio`: 1 minus random mean retained efficiency;
- `random_p05`: released lower empirical order-statistic diagnostic;
- `random_p95`: released upper empirical order-statistic diagnostic;
- `gap_vs_random_mean`: random mean minus targeted retained efficiency;
- `gap_vs_random_p05`: random p05 minus targeted retained efficiency;
- `targeted_below_random_p05`: whether targeted retained efficiency lies below random p05.

## `results/empirical_summary.json`

Machine-readable release summary including:

- source/network counts;
- baseline global efficiency;
- k=30 targeted and random metrics;
- random draw count;
- seed;
- curve invariants;
- gap growth;
- interpretation boundary.

## Important metric note

Retained efficiency can exceed 1.

The post-removal numerator is computed among surviving pairs, so removing peripheral nodes can increase their average inverse path length relative to the intact-network value.

The ratio must not be presented as a bounded survival percentage.
