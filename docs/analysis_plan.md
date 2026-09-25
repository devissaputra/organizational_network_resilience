# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary descriptive target
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Primary operationalization
The release operationalizes communication-network resilience as retained global efficiency among surviving nodes relative to the intact projected network. This is one structural accessibility metric, not a complete measure of organizational resilience.

## Analysis
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removal with 200 seeded random removals at k = 5, 10, 15, 20, and 30.

A retained-efficiency ratio slightly above 1 can occur if removing peripheral nodes increases efficiency among surviving nodes. The ratio is therefore not an organizational performance score or a bounded survival fraction.

## Released diagnostics
For every k, report:
1. targeted retained efficiency;
2. random mean retained efficiency;
3. random 5th and 95th percentile order-statistic bounds;
4. targeted-versus-random mean gap;
5. targeted-versus-random 5th-percentile gap;
6. whether targeted retained efficiency falls below the random 5th percentile.

Across the released curve, targeted retained efficiency is below the random 5th percentile at every k. The targeted-versus-random mean gap rises from 0.0238 at k=5 to 0.1304 at k=30.

These are descriptive distributional diagnostics. They are not presented as a causal effect estimate or a preregistered significance test.

## Missingness / exclusions
All 148 nodes and 10,885 timestamped hyperedges in the published Enron file are included. Repeated recipients within an event are deduplicated for graph projection; no message content, employee role, or knowledge attribute is inferred.

## Extensions not included in this release
Alternative centrality definitions, adaptive re-ranking after each removal, directed or weighted projections, and additional resilience outcomes such as giant-component retention are legitimate follow-up analyses but are not silently represented as completed.

## Interpretation boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.
