# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary estimand / descriptive target
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Analysis
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removals with 200 seeded random removals at k = 5, 10, 15, 20, and 30. Report retained efficiency relative to the intact network. A retained-efficiency ratio slightly above 1 can occur if removing peripheral nodes increases efficiency among the surviving nodes; the ratio is not an organizational performance score.

## Specified outputs for this release
1. source/sample size and provenance;
2. primary derived metric(s);
3. comparator, cross-group, cross-time, or frontier contrast where applicable;
4. uncertainty, sensitivity, or error information supported by the source;
5. explicit construct and external-validity limitations.

## Missingness / exclusions

All 148 nodes and 10,885 timestamped hyperedges in the published Enron file are included. Repeated recipients within an event are deduplicated for graph projection; no message content, employee role, or knowledge attribute is inferred.

## Interpretation boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.
