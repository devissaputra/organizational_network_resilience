# Empirical Study Protocol

## Study title

**Organizational Communication Resilience Under Key-Actor Loss**

## Study type

Secondary observational network stress test using a historical organizational email hypergraph.

This document records the released analysis. It is not a preregistration.

## Research question

How resilient is potential organizational information access to the loss of highly connected communication actors compared with random actor loss?

## Source

email-enron temporal hypergraph, XGI / Zenodo.

Released source identity:

- version v0.1;
- DOI 10.5281/zenodo.21909507;
- file `email-enron.json`;
- MD5 `3666af1fc5a190d93f7fd98cff58e283`.

## Source dimensions

- 148 nodes;
- 10,885 timestamped hyperedges;
- 26,914 released incidences.

## Unit of analysis

Raw unit: timestamped email hyperedge.

Analysis unit: projected communication network under actor removal.

## Projection rule

Each hyperedge is converted into all unique undirected pairwise co-participation ties among its members.

Repeated members within one event are deduplicated.

Repeated co-occurrences across events do not increase edge weight in the released simple graph.

## Baseline

Released projection:

- 148 nodes;
- 2,583 undirected edges;
- global efficiency 0.5601.

## Primary resilience metric

Retained global efficiency:

```text
global efficiency after actor removal
/
global efficiency of intact projection
```

Global efficiency is recomputed on surviving node pairs. Disconnected pairs contribute zero.

A retained-efficiency value above 1 is possible and should not be interpreted as performance above 100%.

## Targeted-removal rule

Rank actors once by degree in the intact projection.

Remove the top k actors for:

```text
k = 5, 10, 15, 20, 30
```

This is a static ranking. Actors are not re-ranked after each removal.

## Random comparator

At each k:

- draw 200 same-count random removal sets;
- seed = 20260925;
- calculate retained efficiency for every draw;
- sort the 200 results;
- report the mean;
- report the released empirical order-statistic bounds corresponding to positions used for p05 and p95.

## Primary outputs

For every k:

- removal count;
- removal fraction;
- targeted retained efficiency;
- targeted loss from intact ratio;
- random mean retained efficiency;
- random mean loss from intact ratio;
- random p05;
- random p95;
- targeted-versus-random mean gap;
- targeted-versus-random p05 gap;
- targeted below random p05 flag.

## Released hypotheses

**H1.** Static degree-targeted removal reduces retained global efficiency faster than same-count random removal.

**H2.** The targeted-versus-random mean gap widens across the released removal levels.

These are released descriptive hypotheses and were not preregistered.

## Released result

Targeted retained efficiency:

```text
0.9735 → 0.9465 → 0.9245 → 0.8986 → 0.8608
```

Random mean:

```text
0.9978 → 0.9970 → 0.9971 → 0.9954 → 0.9917
```

The targeted result is below the released random p05 at every tested k.

## Construct boundary

Email connectivity is treated as a proxy for potential information access.

The study does not measure:

- tacit knowledge;
- expertise;
- trust;
- learning quality;
- knowledge accuracy;
- employee performance;
- causal knowledge transfer.

## Scope boundary

The release uses:

- one historical organization;
- one hypergraph-to-simple-graph projection;
- one centrality targeting rule;
- one resilience metric;
- one static ranking;
- one set of five stress levels.

Alternative specifications are future sensitivity extensions, not hidden completed analyses.
