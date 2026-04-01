import pandas as pd

btc = pd.read_csv("data/silver/btc_clean.csv")
fg = pd.read_csv("data/silver/fear_greed_clean.csv")

# Merge on date
df = pd.merge(btc, fg, on="date")

# Create daily return
df["btc_daily_return"] = df["btc_close"].pct_change()

# Remove NaN from pct_change first row
df = df.dropna()

# Binary variable (important for stats)
df["positive_return"] = (df["btc_daily_return"] > 0).astype(int)

# Save Gold dataset
df.to_csv("data/gold/crypto_gold.csv", index=False)

print("Gold dataset created")

