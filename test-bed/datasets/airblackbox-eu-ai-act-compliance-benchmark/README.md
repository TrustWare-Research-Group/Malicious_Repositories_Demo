# airblackbox-eu-ai-act-compliance-benchmark PoC

Confirms `samples/no_risk_levels_agent.py` wires `execute_shell` (arbitrary `subprocess.run(..., shell=True)`) and `delete_file` (`os.remove`) into a LangChain agent with **no risk classification** - `gpt-4o` can call either tool freely, with zero guardrails, based on nothing but the prompt.

> **This is not a safe, localhost-contained PoC like the other testbed repos.** There's no callback URL to redirect - the payload *is* a real LLM making real decisions. Running it makes genuine `gpt-4o` calls that can actually run shell commands and delete files **on whatever machine you run it on**. Only run this in a disposable VM/container.

## Run

```bash
export OPENAI_API_KEY=sk-...
./run-all-the-flow-once.sh
```

No receiver/monitor step - there's no network callback to capture, the risk is local shell/file access, not exfiltration.

## Manual

```bash
export OPENAI_API_KEY=sk-...
python3 execute-poc.py
```

## Output

Evidence saved to `evidence/airblackbox-eu-ai-act-compliance-benchmark_<timestamp>/`: `run_output.txt` (the agent's tool calls and results - review this before assuming anything was actually deleted).
