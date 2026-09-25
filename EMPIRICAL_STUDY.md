# Empirical Study Protocol

## Study
Organizational Communication Resilience Under Key-Actor Loss

## Research question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Design and source
Secondary observational network analysis of the Enron temporal email hypergraph. Source: email-enron temporal hypergraph (XGI / Zenodo). Analysis/retrieval date: 2026-09-25.

## Hypotheses
1. H1: removing high-degree actors reduces normalized global efficiency faster than removing the same number of randomly selected actors.
2. H2: the targeted-versus-random resilience gap widens as more key actors are removed.

## Operationalization and method
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removals with 200 seeded random removals at k = 5, 10, 15, 20, and 30. Report retained efficiency relative to the intact network.

## Primary empirical result
Targeted removal progressively lowers normalized global efficiency while cost-matched random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

## Validity and claim boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.

## Reproducibility status
The repository packages derived results, study-specific analysis functions, deterministic or seeded procedures where relevant, an internet-enabled source rebuild script, and tests for both computations and critical scientific invariants. The released analysis was documented after dataset selection and should not be represented as preregistered.
