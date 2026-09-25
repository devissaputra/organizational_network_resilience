# Research Bundle Definition

This repository is treated as a research bundle because it links one explicit research question to a named empirical source, a documented operationalization, executable analysis code, derived evidence, reproducibility checks, visual evidence, validity boundaries, and a paper-ready interpretation path.

## Question
How resilient is potential organizational information access to the loss of highly connected employees compared with random employee loss?

## Empirical core
Network global-efficiency stress test with targeted and random node removal.

## Main result
Targeted removal progressively lowers normalized global efficiency while cost-matched random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

## Boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.

## Release criterion
A release passes only if source provenance, code, derived tables, JSON summary, README claims, figures, and tests agree numerically and semantically.
