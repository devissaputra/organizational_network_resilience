# Reproducibility Guide

## Objective

The release supports two verification paths:

1. offline validation from packaged derived evidence;
2. source-to-output reconstruction from the pinned Zenodo dataset.

## Environment

```bash
python -m pip install -r requirements.txt
```

## Offline verification

```bash
pytest -q
python run_demo.py
python scripts/generate_figures.py
```

The offline suite verifies:

- graph projection behavior;
- global-efficiency behavior for connected and disconnected pairs;
- the fact that retained efficiency may exceed 1 after peripheral removal;
- exact removal levels;
- removal fractions;
- targeted and random loss fields;
- monotonic targeted degradation;
- widening targeted-versus-random gaps;
- targeted values below random mean and p05 at all released levels;
- random interval ordering;
- k=30 headline results;
- source identity and checksum metadata;
- random-comparator draw count and seed;
- complete bundle consistency.

## Public-source verification

```bash
python scripts/fetch_and_analyze.py --check
```

The check:

1. downloads `email-enron.json` from the pinned Zenodo record;
2. verifies MD5 `3666af1fc5a190d93f7fd98cff58e283`;
3. reconstructs all 148 source nodes and 10,885 hyperedges;
4. reconstructs the undirected simple projection;
5. recomputes baseline global efficiency;
6. applies the static degree ranking;
7. reruns 200 version-stable deterministic pseudo-random comparators at every k;
8. reconstructs the complete derived CSV and JSON objects;
9. requires exact agreement with the packaged release after documented rounding.

There is no synthetic fallback.

## Regenerating release evidence

```bash
python scripts/fetch_and_analyze.py --write
python scripts/generate_figures.py
```

After regeneration:

```bash
git diff -- data/derived/primary_results.csv results/empirical_summary.json assets/
```

A clean diff indicates the regenerated evidence and figures match the committed release.

## CI

Regular CI runs:

- tests;
- packaged bundle validation;
- scientific figure generation.

The empirical rebuild workflow runs the full Zenodo source check.

## Source identity

- DOI: 10.5281/zenodo.21909507
- version: v0.1
- file: `email-enron.json`
- MD5: `3666af1fc5a190d93f7fd98cff58e283`
- release retrieval date: 2026-09-25

## Reproducibility boundary

Reproducibility confirms this computational operationalization of the pinned source.

It does not validate email connectivity as a direct knowledge measure, prove causal knowledge loss, or establish external validity beyond the historical Enron setting.
