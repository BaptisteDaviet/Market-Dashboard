# Dashboard with equity ($SPY), forex ($DX-Y.NYB), commmodities (Gold ($GC=F), crude oil ($WTI), wheat ($ZW=F)) , bonds ($^TNX) (inflation linked bonds)
# Data about growth, inflation, volatility and yield
# Data goes bask as far as possible w/ widget slider to adjust time frame

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Data Download
def data_download(ticker, filename):
    data = yf.download(ticker, period="max")['Close']
    data.to_csv(filename)

ticker_filename = {
    "SPY": "spy.csv",
    "DX-Y.NYB": "usd.csv",
    "GC=F": "gold.csv",
    "WTI": "wti.csv",
    "ZW=F": "wheat.csv",
    "^TNX": "bonds.csv"
}

sanitized_ticker = {ticker:filename.replace('.csv', '') for ticker, filename in ticker_filename.items()}
# print("Sanitized ticker: ", sanitized_ticker)

data_dict = {}

for ticker, filename in ticker_filename.items():
    data_download(ticker, filename)


# Check for missing values
def check_na(data):
    null_sum = data.isna().sum()
    null_percentage = null_sum/len(data)
    print(f"Ratio of missing values: {null_percentage}\n Count of missing values: {null_sum}")

def fill_missing_values(df):
    """
    filling missing values using FFILL method, input is the Dataframe and output is the filled Dataframe
    """
    df = df.ffill().dropna()
    return df 


def plot_df(ticker):
    data = pd.read_csv(ticker_filename[ticker], index_col=0, parse_dates=True)
    plt.figure()
    plt.title(sanitized_ticker[ticker])
    plt.xlabel("Dates")
    plt.ylabel("")
    plt.plot(data.index, data[ticker])    
    plt.savefig(sanitized_ticker[ticker] + '.png')


for ticker, filename in ticker_filename.items():
    print(f"Checking {ticker}")
    data = pd.read_csv(ticker_filename[ticker], index_col=0, parse_dates=True)
    check_na(data)
    data = fill_missing_values(data)
    plot_df(ticker)


#df.fillna(method='fill) -- this fills in the missing values with the previous day's value (forward fill)

# for ticker, filename in ticker_filename.items():
#     df = pd.read_csv(filename, index_col=0, parse_dates=True)
#     print(f"Checking missing values for {ticker} in {filename}")
#     check_na(df)
    
# for ticker, filename in ticker_filename.items():
#     df = pd.read_csv(filename, index_col=0, parse_dates=True)
#     df.plot(label=ticker)


# plt.title("data")
# plt.xlabel("Time")
# plt.ylabel("Prices")
# plt.legend()
# plt.yscale('log')

# plt.show()




# --------- Future Work ---------
# Write a short function to deal with the missing values
# Scale the data
# Write small functions for each of the data preprocessing steps and them one main function to cacll them all 
# Use streamlit
# Create a function that plot systematically
