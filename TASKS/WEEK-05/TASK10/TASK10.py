import pandas as ps
from pathlib import Path

data_path = Path(__file__).resolve().parents[1] / "TASK9" / "data.json"
df = ps.read_json(data_path)
print(df.head(7))
print(df.tail(7))
