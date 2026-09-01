import pandas as pd
import yfinance as yf

buy_price = 100
sell_price = 105
return_rate = (sell_price - buy_price)/ buy_price
print(return_rate)
print(return_rate*100)

prices = [100, 105, 110, 108]
print(prices)
returns = []
for i  in range(len(prices)-1):
    value = (prices[i+1]- prices[i])/ prices[i]
    returns.append(value)
investment = 100
for r in returns:
    investment= investment*(1+r)

print(investment)
    

data = yf.download("AAPL", start="2025-01-01", end="2026-01-01")
print(data)
# checking the dtaat if it is clean
print(data.info())
print(data.isna().sum())
print(data.index.duplicated().sum())
print(data.index.is_monotonic_increasing)
prices = data[("Close", "AAPL")]

print(prices.describe()) # some statistics

print(data.head())# shows us the  first 5 rows
print(data["Close"].head())
print(data.columns)
prices = data[("Close", "AAPL")]
returns = []
for i in range(len(prices)-1):
    value = (prices.iloc[i+1] - prices.iloc[i])/prices.iloc[i]
    returns.append(value)
print(returns)

returns = prices.pct_change() #Pandas is calculating the percentage change from one day to the next for us.

print(returns.head())

# calculating the moving averages

short_ma = prices.rolling(window = 20).mean() # rolling is a pandas method saying that take 20 prices at a time and calculate their average
long_ma = prices.rolling(window=50).mean()
print(short_ma.head(55))
print(long_ma.head(55))

# we want Pandas to compare them for every date
signal = (short_ma> long_ma).astype(int) # so the comparison gives us a boolen espresion and it us later on changed to the int which is 1 for true and 0 for the false
print(signal.tail(20)) # give me the last 2o rows

# calculating the strategy return
strategy_returns = returns* signal.shift(1) # we are using the yesterday's signal to determine whether we are invested today
# print(strategy_returns.head(60))
# print(signal.value_counts())
# print(signal.tail(20))
# print(strategy_returns.tail(20))

cumulative_returns = (1 + strategy_returns).cumprod()
print(cumulative_returns)