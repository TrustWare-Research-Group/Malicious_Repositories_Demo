# PoC — ysn-rfd/text-dataset-tiny-code-script-py-format

**Flagged file:** [`full_MFE.py`](../../../Dataset/flagged/ysn-rfd__text-dataset-tiny-code-script-py-format/malicious_file_embedding/full_MFE.py)
**Scanner:** opengrep (high — hardcoded default password on `start_keylogger`)

A 6-feature toolkit (AES reverse shell, stego payload embedding,
registry persistence, hidden PowerShell exec, keylogger) behind one CLI.
Two things worth knowing that running the code reveals and neither
scanner caught:

1. `AESCipher.encrypt`/`.decrypt` are broken as shipped —
   `def encrypt(self,  bytes)`: the `data:` annotation got separated from
   the parameter name, so the method body's references to `data` raise
   `NameError`. Every AES-dependent feature (embed/extract, the reverse
   shell, keylogger encryption) is non-functional as distributed here.
2. `run_powershell_script()` calls `os.unlink(tmp.name)` immediately
   after a non-blocking `Popen`, without waiting for PowerShell to open
   the file first — a real race condition, so this demo doesn't always
   win.

[`poc.py`](poc.py) loads the real file and shows both: the `NameError`
from (1), and `run_powershell_script()` actually running a hidden,
silent PowerShell command when it wins the race in (2).

`PersistenceManager.add_registry()` is real and unguarded too (a plain
`winreg.SetValueEx()` under `HKCU\...\Run`)

## Run

```
pip install pycryptodome pynput
python poc.py
```
