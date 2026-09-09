# PoC — torchsight/cybersecurity-classification-benchmark

15 flagged files, 3 families of 5 near-identical samples each (a
classification benchmark's "malicious" class). One script per family,
each naming which file it runs.

| Script | Files | Pattern |
|---|---|---|
| [`poc_sqli.py`](poc_sqli.py) | `sample-0643,0646,0649,0652,0655.py` | f-string SQL query, no parameterization |
| [`poc_shell.py`](poc_shell.py) | `sample-0657,0661,0665,0669,0673.py` | reverse shell to a hardcoded IP:port |
| [`poc_pickle.py`](poc_pickle.py) | `sample-0732,0734,0736,0738,0740.py` | `pickle.loads()` on untrusted bytes |

## Run

```
python poc_sqli.py
python poc_pickle.py

# in one terminal:
nc -lvnp 4444
# in another:
python poc_shell.py
```
