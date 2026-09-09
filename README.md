# Overview

Security testbed for malicious/vulnerable Hugging Face models and datasets -
downloaded artifacts, minimal local safety edits, and working PoC harnesses
that trigger and capture evidence of each vulnerability without depending on
(or reaching out to) the real internet.

## `datasets/`

Sample data pulled from Hugging Face dataset repos that catalog malicious
agent skills and attack techniques - e.g. `samples/zhmzm` and
`samples/XuWY__AgentTrap` (the `AgentTrap` benchmark's flagged "skills",
covering prompt injection, patch injection, OAuth/IAM exfil, and more),
`samples/inclusionAI-A3S-Bench` (malicious file-management skills), and a
few smaller single-technique samples (`applexml`, `UCSC-VLAA`,
`torchsight-cybersecurity-classification-benchmark`). This is reference
data the PoCs in `test-bed/datasets/` load and run against directly - none
of it has been altered from what was downloaded.

## `models/`

Full clones of Hugging Face model repos that ship malicious
`trust_remote_code=True` code or unsafe deserialization vectors - e.g.
`a350h-GoodbyeWorld` (a base64 `exec()` dropper in `modeling.py`) and
`scthornton-bert-tiny-multi-attack-demo` (a pickle RCE payload alongside a
data-exfil vector). Each repo's own `CHANGES.md` documents the one edit made
to it: redirecting its hardcoded callback URL to `127.0.0.1` so triggering
it doesn't call out to a real, live, mutable endpoint. No other logic was
changed.

## `test-bed/`

The actual PoC harnesses - one folder per repo above (under `test-bed/model/`
or `test-bed/datasets/`), each with `execute-poc-*.py` scripts that load and
trigger the real flagged file, plus `receiver.sh` / `monitor.sh` /
`run-all-the-flow-once.sh` to stand up a local receiver, capture the traffic
with `tcpdump`, and save evidence (`capture.pcap`, run output, receiver
output) to that folder's `evidence/`. `requirements.txt` covers the shared
venv (`test-bed/venv/`, gitignored) all of these run against. Each folder's
`README.md` explains how to run it and what to expect.
