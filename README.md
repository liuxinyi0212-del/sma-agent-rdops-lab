# SMA-Agent RDOPS Lab (F01)

Non-production GitHub Actions diagnostic repository. Only synthetic sample data.

## Purpose

The discount calculation is **intentionally wrong** in `src/pricing.py`: it multiplies by `discount` rather than `(1 - discount)`. Two tests will fail. The expected root cause is known, so SMA-Agent's AI diagnosis can be independently assessed.

## Setup

1. Create a new **private** GitHub repository named `sma-agent-rdops-lab` with Actions enabled (do not initialize it with another README if uploading this folder via Git).
2. Commit these files to the default branch. A push triggers `SMA Agent CI Diagnosis Lab`, job `pricing-tests`.
3. Wait until the workflow finishes with `failure`. In GitHub Actions copy the run ID, attempt number, numeric job ID and commit SHA. Use approved read-only access for the SMA-Agent pilot.
4. For the pilot, approve exactly two code paths: `src/pricing.py` and `tests/test_pricing.py`. Keep any GitHub token or DeepSeek API key in secure local configuration, never in the repo.
5. Evaluate the resulting AI diagnosis against the known root cause. **Do not fix the buggy code before first validation.**

## Local test

`python -m pip install pytest && python -m pytest -q tests/test_pricing.py`

Expected: failures in zero and 15% discount tests; invalid discount test passes.

## Safety

No sensitive data, production integrations, network calls from application code, or GitHub write scopes. This is a controlled failing-CI fixture, not production code.
