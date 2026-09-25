# Reproducibility

## Offline verification

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

Offline tests operate on packaged derived evidence and study-specific functions. They verify the five released removal levels, monotonic targeted degradation, widening targeted-versus-random gaps, percentile ordering, summary/CSV agreement, source-version metadata, and the pinned source checksum.

## Full source rebuild

```bash
python scripts/fetch_and_analyze.py
```

The rebuild retrieves the source recorded in `data/source_manifest.json` and verifies MD5 `3666af1fc5a190d93f7fd98cff58e283` before parsing. If the bytes do not match the pinned release, the script stops rather than silently analyzing a different source state. It contains no synthetic fallback.

To regenerate the packaged CSV and JSON outputs after successful checksum verification:

```bash
python scripts/fetch_and_analyze.py --write
```

## CI

`.github/workflows/ci.yml` runs `pytest -q` and `python run_demo.py` on Python 3.10, 3.11, and 3.12 for pushes and pull requests to `main`.

## Reproducibility boundary

External hosting can change or become unavailable. The manifest therefore records the source identity, DOI, dataset version, retrieval date, direct file identity, checksum, and reuse note. Derived results in this release correspond to the pinned source state analyzed on 2026-09-25.
