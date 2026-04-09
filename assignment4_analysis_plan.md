# Assignment 4 Analysis Plan

## 1. New Data Source
For Assignment 4, I added a **holiday dataset** as an external source.  
This dataset contains dates marked as holidays and was used to introduce a new grouping variable.

## 2. Join Key
The holiday dataset was joined with the existing Gold dataset using the **date** column.  
This allowed alignment of Bitcoin data, sentiment data, and holiday information.

## 3. New Variables Created
A new variable called **is_holiday** was created:
- Value = 1 → Holiday  
- Value = 0 → Non-holiday  

Additionally, existing derived variables include:
- btc_daily_return (percentage change in price)
- positive_return (binary indicator of positive return)

## 4. Project Story / Question
This project explores:

> “Do Bitcoin returns and market behavior differ based on sentiment and holidays?”

The goal is to understand whether external factors such as holidays and sentiment influence market performance.

## 5. Planned Statistical Analyses

### 1. One-sample t-test
- Question: Is the mean daily return different from zero?
- Variable: btc_daily_return

### 2. Two-sample t-test
- Question: Do returns differ between holiday and non-holiday days?
- Variables: btc_daily_return, is_holiday

### 3. Chi-square test
- Question: Is positive_return independent of is_holiday?
- Variables: positive_return, is_holiday

### 4. Variance comparison
- Question: Is volatility different between holiday and non-holiday periods?
- Variable: btc_daily_return grouped by is_holiday

### 5. Correlation analysis
- Question: Is sentiment associated with returns?
- Variables: fear_greed_value, btc_daily_return

## 6. Visualizations Supporting Analysis

- Line chart → BTC returns over time  
- Boxplot → Returns grouped by holiday vs non-holiday  
- Scatter plot → Sentiment vs returns  

These visuals help motivate the statistical tests used.

## 7. Justification of Methods

- T-tests are used because we compare means of continuous variables  
- Chi-square is appropriate for categorical variables  
- Variance comparison helps understand volatility differences  
- Correlation measures relationship between two continuous variables  

Each method aligns with the type of data and the research question.

