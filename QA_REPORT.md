# Final QA Report

**Release status: PASS.**

## Checks completed
- public source identity verified against Zenodo record 21909507;
- dataset version v0.1 and DOI recorded;
- source file pinned by MD5 `3666af1fc5a190d93f7fd98cff58e283`;
- raw source is not redistributed because the retrieved Rights section does not display a specific license;
- repository MIT license restored to the complete standard text and recognized by GitHub;
- derived CSV reconciled with `results/empirical_summary.json`;
- targeted-removal curve confirmed to decrease across all five released k values;
- targeted-versus-random mean gap confirmed to widen from 0.0238 to 0.1304;
- targeted retained efficiency confirmed below the random 5th percentile at every released k;
- tests expanded to cover computation, release invariants, summary/table agreement, source version, and checksum;
- `validate_bundle()` strengthened beyond file-presence checks;
- normal GitHub Actions CI added for Python 3.10, 3.11, and 3.12;
- CI completed successfully after the hardening changes;
- checksum-verified source rebuild supports output regeneration with `--write`;
- manual empirical-rebuild workflow added to compare regenerated evidence with the committed release;
- README, protocol, research design, data dictionary, reproducibility guide, and paper blueprint synchronized;
- no synthetic fallback, preregistration claim, causal claim, or hidden alternative-analysis claim is made.

## Final empirical finding
Targeted removal progressively lowers normalized global efficiency while same-count random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

## Required interpretation boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. Global efficiency is one structural operationalization rather than the full construct of organizational resilience, and the Enron setting limits external validity.

## GitHub presentation metadata
The recommended About text and Topics are recorded in `GITHUB_METADATA.md`. Repository-description and Topics are GitHub UI metadata and are not changed by the file-edit connector used for this release.
