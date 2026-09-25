# Empirical Study Protocol

## Study
Organizational Communication Resilience Under Key-Actor Loss

## Research question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Design and source
Secondary observational network analysis of the Enron temporal email hypergraph. The released analysis pins Zenodo record 21909507, dataset version v0.1, DOI 10.5281/zenodo.21909507, and file MD5 `3666af1fc5a190d93f7fd98cff58e283`. Analysis/retrieval date: 2026-09-25.

## Hypotheses
1. H1: removing high-degree actors reduces normalized global efficiency faster than removing the same number of randomly selected actors.
2. H2: the targeted-versus-random resilience gap widens as more key actors are removed.

## Operationalization and method
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removal with 200 seeded random removals at k = 5, 10, 15, 20, and 30. Report retained efficiency relative to the intact network.

Global efficiency is the primary resilience operationalization in this release. It captures shortest-path accessibility among surviving nodes; it does not by itself measure all dimensions of organizational resilience.

## Primary empirical result
Targeted removal progressively lowers normalized global efficiency while same-count random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

Across all five tested removal levels, the targeted retained-efficiency value is below the 5th percentile of the 200-draw random comparator. The targeted-versus-random mean gap widens from 0.0238 at k=5 to 0.1304 at k=30. These are descriptive distributional diagnostics rather than causal or formal inferential claims.

## Validity and claim boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting limits external validity. Alternative centrality definitions, adaptive re-ranking, directed or weighted projections, and additional resilience metrics are not silently treated as completed analyses.

## Reproducibility status
The repository packages derived results, study-specific analysis functions, deterministic or seeded procedures, a checksum-verified internet rebuild script, and tests for numerical consistency, scientific invariants, and provenance. The released analysis was documented after dataset selection and must not be represented as preregistered.
