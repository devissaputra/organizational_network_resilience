# Paper Blueprint

## Working title
Organizational Communication Resilience Under Key-Actor Loss

## Motivation
Succession, turnover, and absence can remove highly connected people from an information network. This study tests whether the observed Enron communication structure is disproportionately dependent on high-degree actors while keeping the construct claim limited to communication connectivity.

## Research question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Data and method
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removal with 200 seeded same-count random removals at k = 5, 10, 15, 20, and 30. Report retained efficiency relative to the intact network.

## Results to report
Targeted removal progressively lowers normalized global efficiency while same-count random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

Report the full five-level table, not only the strongest contrast. Across every tested k, targeted retained efficiency is below the random 5th percentile. The targeted-versus-random mean gap widens from 0.0238 at k=5 to 0.1304 at k=30.

## Robustness / sensitivity
The released study includes a 200-draw seeded random comparator and its 5th-95th percentile diagnostic band at every k. This supports a descriptive distributional comparison, not a causal or formal significance claim.

Alternative centrality definitions, adaptive re-ranking after each removal, directed or weighted projections, and additional resilience outcomes would be post hoc extensions and must be labeled as such if added later.

## Limitations
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. Global efficiency is a single structural metric, and the Enron setting limits external validity.

## Publication integrity
Do not describe this repository as peer reviewed, preregistered, causal, or externally validated unless those events actually occur. Distinguish analysis of public data from original data collection.
