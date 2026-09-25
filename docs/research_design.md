# Research Design

## Research question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Design
Secondary observational network analysis of the Enron temporal email hypergraph.

## Source and unit of analysis
Source: email-enron temporal hypergraph (XGI / Zenodo), version v0.1, DOI 10.5281/zenodo.21909507. The release pins `email-enron.json` by MD5 `3666af1fc5a190d93f7fd98cff58e283`. The operational unit follows the public dataset and is documented in `data/source_manifest.json` and `docs/data_dictionary.md`.

## Hypotheses
1. H1: removing high-degree actors reduces normalized global efficiency faster than removing the same number of randomly selected actors.
2. H2: the targeted-versus-random resilience gap widens as more key actors are removed.

## Method
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removals with 200 seeded same-count random removals at k = 5, 10, 15, 20, and 30.

Global efficiency is recomputed among surviving nodes and normalized to the intact-network value. A retained-efficiency ratio slightly above 1 can occur if removal of peripheral nodes shortens paths among survivors; the ratio is not an organizational performance score.

## Released distributional diagnostic
At each tested k, report the targeted value, random mean, random 5th and 95th percentile order-statistic bounds, the targeted-versus-random gaps, and whether the targeted value falls below the random 5th percentile. In the released results, it does so at all five k values.

## Validity boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. Global efficiency is a single structural operationalization, and the Enron setting limits external validity. Alternative centrality rules, graph representations, and resilience outcomes remain follow-up analyses.
