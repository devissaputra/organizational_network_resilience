# Data Dictionary

## Provenance
See `data/source_manifest.json`. The release pins Zenodo dataset version v0.1 and source-file MD5 `3666af1fc5a190d93f7fd98cff58e283`. Raw source observations are not republished in this repository.

## `data/derived/primary_results.csv`
Complete five-level removal curve used in the reported analysis.

Columns:
- `removed`: number of removed nodes;
- `targeted_retained_efficiency`: efficiency after static degree-targeted removal divided by intact-network efficiency;
- `random_mean`: mean retained efficiency across 200 seeded same-count random removals;
- `random_p05`: 5th-percentile order-statistic diagnostic from the 200 random draws;
- `random_p95`: 95th-percentile order-statistic diagnostic from the 200 random draws;
- `gap_vs_random_mean`: random mean minus targeted retained efficiency;
- `gap_vs_random_p05`: random 5th percentile minus targeted retained efficiency;
- `targeted_below_random_p05`: whether targeted retained efficiency is below the random 5th percentile.

## `results/empirical_summary.json`
Machine-readable headline sample sizes, release estimates, random-draw count, seed, and robustness diagnostics. Values must agree with README text and the derived CSV.

## Construct boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. Global efficiency is one structural operationalization, not the full organizational-resilience construct.
