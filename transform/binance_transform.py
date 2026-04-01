import json
import pandas as pd
import glob

files = glob.glob("data/bronze/binance_*.json")
latest_file = sorted(files)[-1]

with open(latest_file) as f:
    raw = json.load(f)

df = pd.DataFrame(raw, columns=[
    "open_time","open","high","low","close","volume",
    "close_time","qav","trades","tb_base","tb_quote","ignore"
])

df["date"] = pd.to_datetime(df["open_time"], unit="ms").dt.date
df["btc_close"] = df["close"].astype(float)
df["btc_volume"] = df["volume"].astype(float)

silver = df[["date","btc_close","btc_volume"]]

silver.to_csv("data/silver/btc_clean.csv", index=False)

print("Binance Silver done")

