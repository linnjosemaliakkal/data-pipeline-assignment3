import streamlit as st
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/gold/crypto_gold.csv")

st.title("📊 Crypto Market Analysis Dashboard")

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.header("Dataset Preview")
st.write(df.head())

st.write("Summary Statistics")
st.write(df.describe())

st.markdown("---")

# ✅ HOLIDAY COLUMN CHECK
st.header("✅ Holiday Column Check")
if "is_holiday" in df.columns:
    st.success("✅ is_holiday column exists!")
    holiday_counts = df["is_holiday"].value_counts()
    st.write("Holiday counts:")
    st.write(holiday_counts)
else:
    st.error("❌ is_holiday column missing - merge failed!")

# -----------------------------
# VISUALS
# -----------------------------
st.header("Visual Analysis")

# Time series
st.subheader("BTC Daily Returns Over Time")
st.line_chart(df["btc_daily_return"])

# Boxplot
st.subheader("Holiday vs Non-Holiday Returns")
fig, ax = plt.subplots()
df.boxplot(column="btc_daily_return", by="is_holiday", ax=ax)
st.pyplot(fig)

# Scatter plot
st.subheader("Fear & Greed vs Returns")
fig2, ax2 = plt.subplots()
ax2.scatter(df["fear_greed_value"], df["btc_daily_return"])
ax2.set_xlabel("Fear & Greed Index")
ax2.set_ylabel("BTC Daily Return")
st.pyplot(fig2)

# -----------------------------
# STATISTICAL TESTS
# -----------------------------
st.header("Statistical Analysis")

# 1. One-sample t-test
st.subheader("1. One-Sample T-Test")
t_stat, p_val = stats.ttest_1samp(df["btc_daily_return"], 0)
st.write("P-value:", p_val)

# 2. Two-sample t-test
st.subheader("2. Two-Sample T-Test (Holiday vs Non-Holiday)")
holiday = df[df["is_holiday"] == 1]["btc_daily_return"]
non_holiday = df[df["is_holiday"] == 0]["btc_daily_return"]

t_stat2, p_val2 = stats.ttest_ind(holiday, non_holiday, equal_var=False)
st.write("P-value:", p_val2)

# 3. Chi-square test
st.subheader("3. Chi-Square Test")
contingency = pd.crosstab(df["positive_return"], df["is_holiday"])
chi2, p, dof, exp = stats.chi2_contingency(contingency)
st.write("P-value:", p)

# 4. Variance test (F-test)
st.subheader("4. Variance Comparison")
var1 = holiday.var()
var2 = non_holiday.var()
f_stat = var1 / var2
st.write("F-statistic:", f_stat)

# 5. Correlation
st.subheader("5. Correlation Analysis")
corr, p_corr = stats.pearsonr(df["fear_greed_value"], df["btc_daily_return"])
st.write("Correlation:", corr)
st.write("P-value:", p_corr)

# -----------------------------
# INTERPRETATION
# -----------------------------
st.header("Interpretation")
st.write("""
- T-test shows whether average returns differ from zero
- Holiday comparison checks behavioral differences
- Chi-square tests independence of returns and holidays
- Variance test compares volatility
- Correlation shows relationship between sentiment and returns
""")

st.markdown("---")

st.header("Conclusion")

st.write("""
This analysis explores whether Bitcoin returns are influenced by market sentiment and holidays.

The results suggest:
- Returns fluctuate regardless of holidays
- Sentiment may have some relationship with returns
- However, statistical significance does not imply causation

This analysis is limited by dataset size and external factors not included.
""")
