
from pathlib import Path
import nbformat
from nbclient import NotebookClient

NOTEBOOKS = [
    Path("01_notebook_variables.ipynb"),
    Path("02_list_loop_if.ipynb"),
    Path("03_ai_code_reading.ipynb"),
]

for notebook_path in NOTEBOOKS:
    with notebook_path.open("r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    client = NotebookClient(
        notebook,
        timeout=120,
        kernel_name="python3",
        allow_errors=False,
    )
    client.execute()
    print(f"OK: {notebook_path}")
