# Dashboard with equity (SPY), forex (USD), commmodities (gold, crude oil, wheat), bonds (inflation linked bonds)
# Data about growth, inflation, volatility and yield
# Data goes bask as far as possible w/ widget slider to adjust time frame

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Getting the data for SPY (daily)
# Closing prices only
# data = yf.download("SPY", period="max")['Close']
# data.to_csv("spy_data.csv")
# print(data.index)
# print('\n\n')

# Data Download
def data_download(ticker, filename):
    data = yf.download(ticker)['Close']
    data.to_csv(filename)

ticker_filename = {
    "SPY": "spy.csv",
    "DX-Y.NYB": "usd.csv",
    "GC=F": "gold.csv",
    "WTI": "wti.csv",
    "ZW=F": "wheat.csv",
    "^TNX": "bonds.csv"
}

for ticker, filename in ticker_filename.items():
    data_download(ticker, filename)


# Sanity Check
# Check for missing values
def check_na(data):
    null_sum = data.isna().sum()
    null_percentage = null_sum/len(data)
    print(f"Ratio of missing values: {null_percentage}\n Count of missing values: {null_sum}")


#df.fillna(method='fill) -- this fills in the missing values with the previous day's value (forward fill)
#spy = (pd.read_csv("spy_data.csv", index_col=0, parse_dates=True)['SPY'].pct_change() + 1).cumprod()

spy = (pd.read_csv("spy.csv", index_col=0, parse_dates=True))
check_na(spy)
       
                   
# # Forex using USD index
# usd = (yf.download('DX-Y.NYB', start=spy.index.min())['Close'].pct_change() + 1).cumprod()
# usd['DX-Y.NYB'].plot(label='USD Index')

# Chech for missing values 
# missing_values = data.isna().sum() # number is zero, no missing values 

# Plot the data
# spy.plot()
# plt.ylabel("SPY Closing Prices Over Time")
# plt.title("SPY Closing Prices")
# plt.yscale('log')


# plt.legend()
# plt.show()


# -------- Future Work -------- 
# Write function to deal with missing values
# Scale the data
# 