import pandas as pd

# Load cleaned datasets
btc = pd.read_csv("data/silver/btc_clean.csv")
fg = pd.read_csv("data/silver/fear_greed_clean.csv")

# Load NEW external dataset (holidays)
holidays = pd.read_csv("data/silver/holidays.csv")

# Ensure date format
btc["date"] = pd.to_datetime(btc["date"])
fg["date"] = pd.to_datetime(fg["date"])
holidays["date"] = pd.to_datetime(holidays["date"])

# Merge datasets
df = pd.merge(btc, fg, on="date")
df = pd.merge(df, holidays, on="date", how="left")

# Fill missing holiday values
df["is_holiday"] = df["is_holiday"].fillna(0).astype(int)

# Create daily return
df["btc_daily_return"] = df["btc_close"].pct_change()

# Remove NaN
df = df.dropna()

# Binary variable
df["positive_return"] = (df["btc_daily_return"] > 0).astype(int)

# Save Gold dataset
df.to_csv("data/gold/crypto_gold.csv", index=False)

print("Gold dataset created successfully")
