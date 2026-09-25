# Research Bundle Definition

This repository is treated as a research bundle because it links one explicit research question to a named empirical source, a documented operationalization, executable analysis code, derived evidence, reproducibility checks, visual evidence, validity boundaries, and a paper-ready interpretation path.

## Question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Empirical core
Network global-efficiency stress test with static degree-targeted node removal and a 200-draw seeded same-count random comparator.

## Main result
Targeted removal progressively lowers normalized global efficiency while same-count random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

Across all five tested removal levels, the targeted retained-efficiency value is below the random 5th percentile. The targeted-versus-random mean gap widens from 0.0238 at k=5 to 0.1304 at k=30.

## Source integrity
The release pins Zenodo dataset version v0.1, DOI 10.5281/zenodo.21909507, and source-file MD5 `3666af1fc5a190d93f7fd98cff58e283`. The full rebuild stops if the downloaded bytes do not match the pinned source.

## Boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. Global efficiency is one structural operationalization rather than a complete organizational-resilience measure. The Enron setting also limits external validity.

## Release criterion
A release passes only if source provenance, pinned file identity, code, derived tables, JSON summary, README claims, tests, and documented interpretation agree numerically and semantically. Normal CI validates the packaged bundle; the manual empirical-rebuild workflow verifies source-to-output regeneration.
