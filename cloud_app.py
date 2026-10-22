"""Public deployment entrypoint: no shared data replacement by visitors."""
import os
import runpy
from pathlib import Path

os.environ["CTD_ALLOW_IID_IMPORT"] = "0"
runpy.run_path(str(Path(__file__).with_name("app.py")), run_name="__main__")
