import os
import subprocess

SCRIPT = os.path.expanduser(
    "~/repos/datasets/samples/torchsight/malicious/sample-0669.py"
)

env = {
    "HOME": "/tmp/fake-home",
    "PATH": "/usr/bin:/bin",
    "FAKE_SECRET": "canary-12345",
}

# this connects out and spawns /bin/sh -i tied to the socket - it blocks until
# the receiving end sends "exit" (see auto_receiver.sh) or closes the connection
subprocess.run(["python3", SCRIPT], env=env)
