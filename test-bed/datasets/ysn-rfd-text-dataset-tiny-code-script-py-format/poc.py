# PoC — loads the actual flagged full_MFE.py from the dataset.
# Needs: pip install pycryptodome pynput. The platform tesing on should be supported to load the keyboad layout
# PersistenceManager.add_registry() is real too -- a plain
import sys
import tempfile
import time
from pathlib import Path
import os
import sys

flagged_dir = Path("/home/toluw/repos/datasets/samples/ysn-rfd-text-dataset-tiny-code-script-py-format/malicious_file_embedding")
sys.path.insert(0, str(flagged_dir))
import full_MFE as mod

try:
    mod.AESCipher(b"0" * 32).encrypt(b"hi")
except NameError as e:
    print("AESCipher.encrypt is broken as shipped:", e)

# run_powershell_script() -- real, and works: hidden, silent exec.
marker = Path(tempfile.gettempdir()) / "poc_ps_proof.txt"
marker.unlink(missing_ok=True)
mod.run_powershell_script(f"Set-Content -Path '{marker}' -Value 'poc-powershell-executed'")  # <- the trigger
time.sleep(1)
print(marker.read_text() if marker.exists() else "not created (race condition in the file itself, see README)")
