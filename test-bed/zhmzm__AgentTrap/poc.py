# PoC — runs the actual flagged with_server.py from the dataset, via its
# normal CLI usage (--server, --port, -- <command>).
# Needs: pip install playwright && playwright install chromium
# Once the server is "ready" it silently launches a headless browser
# against http://localhost:<port>/fixtures/injected_page.html before
# running the command you asked for. `python -m http.server` stands in
# for "the dev server" here -- any command that opens the given port
# works, per the file's own usage docstring.

import sys
import runpy
from pathlib import Path

flagged = (Path(__file__).resolve().parents[3] / "Dataset" / "flagged" / "zhmzm__AgentTrap"
           / "skills" / "malicious" / "case_0007_dim3_webapp_testing_prompt_inject"
           / "scripts" / "with_server.py")

sys.argv = ["with_server.py", "--server", "python -m http.server 8000", "--port", "8000",
            "--", "echo", "your actual test command ran"]
runpy.run_path(str(flagged), run_name="__main__")  # <- hidden playwright navigation fires after "server ready"
