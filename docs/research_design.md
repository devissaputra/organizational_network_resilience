# Research Design

## Research question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Design
Secondary observational network analysis of the Enron temporal email hypergraph.

## Source and unit of analysis
Source: email-enron temporal hypergraph (XGI / Zenodo). The operational unit follows the public dataset and is documented in `data/source_manifest.json` and `docs/data_dictionary.md`.

## Hypotheses
1. H1: removing high-degree actors reduces normalized global efficiency faster than removing the same number of randomly selected actors.
2. H2: the targeted-versus-random resilience gap widens as more key actors are removed.

## Method
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removals with 200 seeded random removals at k = 5, 10, 15, 20, and 30. Report retained efficiency relative to the intact network. A retained-efficiency ratio slightly above 1 can occur if removing peripheral nodes increases efficiency among the surviving nodes; the ratio is not an organizational performance score.

## Validity boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.
