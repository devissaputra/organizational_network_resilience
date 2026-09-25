# Analysis Plan

## Status

This document records the released secondary analysis.

It is not a preregistration.

## Primary question

How resilient is potential organizational information access to the loss of highly connected communication actors compared with same-count random actor loss?

## Data transformation

1. read the pinned temporal email hypergraph;
2. retain all 148 nodes;
3. group incidences by email hyperedge;
4. deduplicate repeated members inside each hyperedge;
5. project each hyperedge into all unique undirected pairwise ties;
6. collapse repeated co-participation into a simple graph.

## Baseline network outputs

Report:

- nodes;
- hyperedges;
- incidences;
- projection edges;
- intact-network global efficiency.

## Primary resilience operationalization

```text
retained efficiency =
efficiency after removal /
intact-network efficiency
```

Efficiency is recomputed among surviving nodes.

A value above 1 is mathematically possible and is not treated as performance above 100%.

## Targeted stress test

Rank actors once by degree in the intact projection.

Remove the top k actors for:

```text
5, 10, 15, 20, 30
```

Report both actor count and fraction of the 148-node source network.

The ranking is static rather than adaptive.

## Random comparator

For every k:

- draw 200 random same-count actor sets;
- use seed 20260925;
- compute retained efficiency for each draw;
- sort the draw values;
- report the mean;
- report released empirical order-statistic p05 and p95 bounds.

These bands are descriptive random-comparator bounds rather than confidence intervals.

## Released outputs

For each k:

1. removal count;
2. removal fraction;
3. targeted retained efficiency;
4. targeted loss from baseline ratio;
5. random mean retained efficiency;
6. random mean loss from baseline ratio;
7. random p05;
8. random p95;
9. gap versus random mean;
10. gap versus random p05;
11. targeted-below-random-p05 indicator.

## Released diagnostics

The package tests whether:

- targeted retained efficiency decreases monotonically;
- targeted result is below random mean at every k;
- targeted result is below random p05 at every k;
- the targeted-versus-random mean gap widens monotonically;
- random p05 ≤ mean ≤ p95.

## Interpretation

The primary inferential object is **structural network accessibility**.

The analysis does not observe tacit knowledge, expertise, trust, learning, employee value, or business performance.

## Extensions not included

Not silently completed in this release:

- adaptive degree re-ranking;
- betweenness or other centrality targeting;
- directed projection;
- weighted projection;
- temporal stress testing;
- hypergraph-native resilience metrics;
- largest-component retention;
- employee-role analysis;
- message-content analysis.
