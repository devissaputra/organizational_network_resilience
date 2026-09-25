# Final QA Report

## Release verdict

**Status: PASS after the full Learning and Development research-package rebuild.**

This file records release consistency. The scientific narrative is in [REPORT.md](REPORT.md).

## Source verification

Verified against Zenodo record 21909507:

- dataset: email-enron;
- version: v0.1;
- published: 12 August 2026;
- DOI: 10.5281/zenodo.21909507;
- file: email-enron.json;
- MD5: 3666af1fc5a190d93f7fd98cff58e283;
- nodes: 148;
- timestamped hyperedges: 10,885.

The source page describes one connected component of 143 nodes and five isolates.

## Released network evidence

| Check | Value | Status |
|---|---:|---|
| Nodes | 148 | PASS |
| Hyperedges | 10,885 | PASS |
| Incidences | 26,914 | PASS |
| Projection edges | 2,583 | PASS |
| Baseline global efficiency | 0.5601 | PASS |
| Random draws per k | 200 | PASS |
| Seed | 20260925 | PASS |
| Removal levels | 5, 10, 15, 20, 30 | PASS |

## Stress-curve verification

Targeted retained efficiency:

- k=5: 0.9735
- k=10: 0.9465
- k=15: 0.9245
- k=20: 0.8986
- k=30: 0.8608

Random mean retained efficiency:

- k=5: 0.9973
- k=10: 0.9970
- k=15: 0.9968
- k=20: 0.9960
- k=30: 0.9912

## Scientific invariants

The released package verifies that:

- targeted retained efficiency decreases at every tested k;
- targeted retained efficiency is below the random mean at every tested k;
- targeted retained efficiency is below random p05 at every tested k;
- the targeted-versus-random mean gap widens at every tested k;
- the random p05, mean, and p95 ordering is valid;
- the final gap is 0.1304;
- all CSV and JSON headline values agree.

## Scientific presentation improvements

The rebuild:

- adds a full `REPORT.md`;
- expands the paper blueprint;
- converts the main figure into a real empirical stress-test visualization;
- rebuilds the method and evidence figures with scientific color;
- adds a reproducible figure generator;
- expands the derived table with removal fractions and explicit loss-from-baseline fields;
- makes static ranking and projection loss explicit;
- strengthens the L&D knowledge-continuity interpretation while preserving the construct boundary;
- updates the public portfolio explanation;
- changes the public Report MD link from QA evidence to the scientific report.

## Interpretation boundary

Email connectivity is a proxy for potential structural information access.

The release does not measure tacit knowledge, expertise quality, employee value, learning effectiveness, causal knowledge transfer, or business-performance loss.

## Reproducibility

PASS requires:

- offline tests;
- bundle validation;
- reproducible SVG generation;
- source checksum verification;
- source-to-output rebuild agreement;
- synchronized documentation and machine-readable results.

## Final assessment

The repository is suitable as a professor-facing L&D research artifact for its declared secondary-analysis scope.

PASS does not imply publication peer review or external organizational validation.
