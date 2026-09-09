# PoC — runs the actual flagged sample-0657.py from the dataset
# (representative of sample-0657/0661/0665/0669/0673.py, all identical).
# No extra deps.
# Real code connects to a hardcoded C2 IP then execs /bin/sh -i over the
# socket. socket.connect() is redirected to localhost so you can catch it
# yourself instead of reaching the (presumably dead) real C2:
#   in another terminal: nc -lvnp 4444
# POSIX only (/bin/sh) -- won't work on native Windows.

import socket
import runpy
from pathlib import Path

real_connect = socket.socket.connect
socket.socket.connect = lambda self, addr: real_connect(self, ("127.0.0.1", 4444))

flagged = (Path(__file__).resolve().parents[3] / "Dataset" / "flagged"
           / "torchsight__cybersecurity-classification-benchmark" / "malicious" / "sample-0657.py")
runpy.run_path(str(flagged), run_name="__main__")  # <- connects to 127.0.0.1:4444, spawns /bin/sh -i over it
