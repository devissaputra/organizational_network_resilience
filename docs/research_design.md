# Research Design

## Decision problem

Headcount loss does not reveal whether the removed people occupied ordinary or structurally central communication positions.

The study therefore asks whether potential communication accessibility is disproportionately sensitive to highly connected actor loss.

## Portfolio framing

This repository belongs to **Learning & Development Research**.

Its practical relevance is knowledge continuity, succession, cross-training, mentoring redundancy, documentation, communities of practice, and access to expertise.

The network itself does not identify which intervention is appropriate.

## Source

email-enron temporal hypergraph, XGI / Zenodo v0.1.

DOI:

`10.5281/zenodo.21909507`

## Raw representation

A node is an email address from the source's core Enron set.

A timestamped hyperedge contains the sender and recipients of one email event.

## Projection design

The released analysis converts every hyperedge to undirected pairwise co-participation ties.

This gives a simple graph suitable for shortest-path global efficiency.

The projection intentionally discards:

- sender direction;
- interaction frequency;
- timestamps;
- message content;
- higher-order group structure.

Those losses are part of the validity boundary.

## Resilience design

### Baseline

Compute intact-network global efficiency.

### Targeted stress

Rank nodes once by intact-network degree and remove the top k.

### Random benchmark

Compare with 200 seeded same-count random removal sets at each k.

### Stress levels

5, 10, 15, 20, and 30 nodes.

## Why global efficiency

Global efficiency summarizes shortest-path accessibility and remains defined for disconnected graphs because unreachable pairs contribute zero.

The metric is useful for structural accessibility but is not a complete organizational-resilience construct.

## Distributional comparison

The random comparator provides:

- mean;
- p05 order statistic;
- p95 order statistic.

The targeted curve is interpreted relative to this released distribution, not only relative to one random sample.

## Construct boundary

Communication connectivity is a proxy for potential information access.

It is not direct measurement of:

- knowledge;
- expertise;
- trust;
- learning;
- performance;
- replaceability.

## External-validity boundary

Enron is historically unusual.

The source contains a core set of addresses and reflects historical correction, redaction, deletion, and corpus preparation.

Findings should not be generalized automatically to contemporary organizations.
