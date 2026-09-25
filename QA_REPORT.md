# Final QA Report

**Release status: PASS after correction.**

## Checks completed
- provenance and source identity reviewed;
- licensing/reuse note recorded;
- derived CSV structure checked against the stated sample and estimand;
- `results/empirical_summary.json` reconciled with packaged evidence;
- README/report language reconciled with the numerical results;
- study-specific methods moved into `research/model.py`;
- tests exercise scientific logic and invariants;
- internet rebuild script has no synthetic fallback;
- four SVG assets regenerated as study-specific figures and XML-validated;
- local Markdown links checked;
- citation metadata points to the final repository slug;
- no preregistration claim is made.

## Final empirical finding
Targeted removal progressively lowers normalized global efficiency while cost-matched random removal leaves mean efficiency close to baseline. At 30 removals, targeted retained efficiency is 0.8608 versus 0.9912 under random removal.

## Required interpretation boundary
Email connectivity is a proxy for potential information access, not a direct measure of tacit knowledge, expertise, performance, or causal knowledge transfer. The Enron setting also limits external validity.
