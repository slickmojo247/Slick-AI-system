import csv
from pathlib import Path

def load_session(session_path: str):
    if not Path(session_path).exists():
        return []
    with open(session_path, 'r') as f:
        return list(csv.reader(f))
