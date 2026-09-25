# Paper Blueprint

## Working title
Organizational Communication Resilience Under Key-Actor Loss

## Motivation
Succession, turnover, and absence can remove highly connected people from an information network. This study tests whether the observed Enron communication structure is disproportionately dependent on high-degree actors while keeping the construct claim limited to communication connectivity.

## Research question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Data and method
Project each email hyperedge into an undirected employee co-participation graph, compute baseline global efficiency, rank actors by projection degree, then compare degree-targeted removals with 200 seeded random removals at k = 5, 10, 15, 20, and 30. Report retained efficiency relative to the intact network.

## Results to report
Targeted removal progressively lowers normalized global efficiency while cost-matched random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal. Report the packaged headline metrics and the full relevant derived table; do not cherry-pick only the strongest contrast.

## Robustness / sensitivity
The released analysis compares targeted removal with 200 seeded random removals at every k and reports the random 5th–95th percentile band. The targeted curve should be interpreted against that distribution, not against a single random draw. Alternative centrality definitions, adaptive re-ranking after each removal, or directed/weighted projections would be additional post hoc analyses, not part of this release.

## Limitations
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.

## Publication integrity
Do not describe this repository as peer reviewed, preregistered, or externally validated unless those events actually occur. Distinguish analysis of public data from original data collection.
