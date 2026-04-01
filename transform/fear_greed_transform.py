import json
import pandas as pd
import glob

files = glob.glob("data/bronze/fear_greed_*.json")
latest_file = sorted(files)[-1]

with open(latest_file) as f:
    raw = json.load(f)

data = raw["data"]

df = pd.DataFrame(data)

df["timestamp"] = pd.to_numeric(df["timestamp"], errors="coerce")
df["date"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce").dt.date
df["fear_greed_value"] = df["value"].astype(int)
df["fear_greed_label"] = df["value_classification"]

silver = df[["date","fear_greed_value","fear_greed_label"]]

silver.to_csv("data/silver/fear_greed_clean.csv", index=False)

print("Fear & Greed Silver done")

