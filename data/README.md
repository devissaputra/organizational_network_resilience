# Data Provenance and Derived Evidence

## Canonical source

**email-enron temporal hypergraph, XGI / Zenodo**

- version: v0.1
- DOI: 10.5281/zenodo.21909507
- published: 2026-08-12
- file: `email-enron.json`
- MD5: `3666af1fc5a190d93f7fd98cff58e283`

## Source description

The dataset contains:

- 148 nodes;
- 10,885 timestamped hyperedges;
- one connected component of size 143;
- five isolates.

Nodes are email addresses in a core Enron set.

A hyperedge contains the sender and recipients of an email event.

## Historical source caveat

The dataset descends from the Enron email corpus, which underwent correction and cleaning after release. The current source also reflects historical deletion and redaction decisions.

## Raw-file policy

The Zenodo record is marked Open, but its displayed Rights section does not show a specific license value.

The repository therefore does not redistribute the raw JSON.

## Packaged derived evidence

`derived/primary_results.csv` contains the complete five-level resilience curve and comparator diagnostics.

## Rebuild

```bash
python scripts/fetch_and_analyze.py --check
```

The source rebuild verifies the pinned MD5 before reconstructing the release.

There is no synthetic fallback.

## Construct boundary

Email connectivity is a proxy for potential structural information access.

It is not direct evidence of tacit knowledge, expertise, learning, trust, employee value, or causal performance.
