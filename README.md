# Organizational Communication Resilience Under Key-Actor Loss

[![CI](https://github.com/devissaputra/organizational_network_resilience/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/organizational_network_resilience/actions/workflows/ci.yml)

> **Empirical Research Bundle** · **Portfolio Track: Learning & Development Research** · Organizational Learning / Knowledge Resilience / Network Analysis

Empirical Enron communication-network resilience study comparing degree-targeted key-actor loss with same-count random removal.

![Empirical workflow](assets/architecture.svg)

## Study status

**Completed secondary empirical analysis.** Reported findings were calculated from the pinned public source on 25 September 2026. The rebuild script contains **no synthetic fallback** and verifies the source file checksum before analysis. Raw source data are not republished; `data/source_manifest.json` records provenance, version, checksum, reuse notes, and the claim boundary.

## Research question

> How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Design

- **Design:** Secondary observational network analysis of the Enron temporal email hypergraph
- **Source:** email-enron temporal hypergraph (XGI / Zenodo)
- **Dataset version:** v0.1
- **Source page:** https://zenodo.org/records/21909507
- **DOI:** 10.5281/zenodo.21909507
- **Pinned file MD5:** `3666af1fc5a190d93f7fd98cff58e283`
- **Retrieval / analysis date:** 2026-09-25
- **Reuse note:** Zenodo marks the record as Open, but the retrieved Rights section does not display a specific license. This repository therefore does not redistribute the raw file; users should follow the Zenodo record and original-source terms.

## Hypotheses

1. H1: removing high-degree actors reduces normalized global efficiency faster than removing the same number of randomly selected actors.
2. H2: the targeted-versus-random resilience gap widens as more key actors are removed.

## Empirical method

Each email hyperedge is projected into an undirected employee co-participation graph. The analysis computes baseline global efficiency, ranks actors by projection degree, and compares degree-targeted removal with 200 seeded random removals at k = 5, 10, 15, 20, and 30. The primary outcome is retained global efficiency relative to the intact network.

**Metric note:** global efficiency is recomputed on surviving-node pairs and then divided by the intact-network value. A retained-efficiency ratio slightly above 1 can occur when removing peripheral nodes shortens average paths among survivors. It is not an organizational performance score or a bounded survival fraction.

![Method](assets/method.svg)

## Headline empirical finding

Targeted removal progressively lowers normalized global efficiency while same-count random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is **0.8608** versus **0.9912** under random removal.

### Headline metrics

- **nodes:** 148
- **hyperedges:** 10,885
- **incidences:** 26,914
- **projection edges:** 2,583
- **baseline global efficiency:** 0.5601
- **targeted retained efficiency, k=30:** 0.8608
- **random mean retained efficiency, k=30:** 0.9912

### Distributional robustness diagnostic

The released random comparator contains 200 seeded draws at every removal level. The targeted retained-efficiency value is **below the random 5th percentile at all five tested k values**. The targeted-versus-random mean gap increases from **0.0238 at k=5** to **0.1304 at k=30**.

This is a descriptive distributional diagnostic, not a causal estimate and not a substitute for a formal inferential design. The released study uses **global efficiency as its primary resilience operationalization**; alternative centrality rules, adaptive re-ranking, directed/weighted projections, and additional resilience outcomes remain extensions rather than hidden analyses.

The complete five-level table is in `data/derived/primary_results.csv` and documented in `docs/data_dictionary.md`.

![Research evidence](assets/research_design.svg)

## What this study can and cannot claim

**Can claim:** the computations in this repository summarize the named, pinned public dataset under the documented operationalization.

**Cannot claim:** email connectivity directly measures tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting limits external validity, and one graph metric does not exhaust the broader construct of organizational resilience.

![Finding and boundary](assets/evaluation.svg)

## Reproduce

Offline verification of packaged empirical results:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

Recompute from the pinned public source after checksum verification:

```bash
python scripts/fetch_and_analyze.py
```

Regenerate the packaged CSV and JSON outputs:

```bash
python scripts/fetch_and_analyze.py --write
```

GitHub Actions runs the offline test and bundle-validation suite on Python 3.10, 3.11, and 3.12.

## Research bundle contents

- `README.md` — study overview and bounded findings
- `EMPIRICAL_STUDY.md` — protocol, validity, and interpretation
- `data/source_manifest.json` — pinned provenance, checksum, reuse note, and claim boundary
- `data/derived/primary_results.csv` — complete five-level release curve and diagnostics
- `results/empirical_summary.json` — machine-readable headline results
- `scripts/fetch_and_analyze.py` — checksum-verified public-source rebuild
- `research/model.py` — reusable study-specific analysis and validation functions
- `tests/` — behavioral, numerical-consistency, and provenance tests
- `.github/workflows/ci.yml` — automated CI
- `docs/` — analysis plan, data dictionary, paper blueprint, references, originality map
- `assets/` — four study-specific SVG figures

## Research integrity

This bundle distinguishes **source data**, **operationalization**, **result**, and **interpretation**. The analysis plan documents the released analysis; it is **not a preregistration**. Public data do not automatically validate a construct, so proxy, single-metric, and external-validity limits are explicit.
