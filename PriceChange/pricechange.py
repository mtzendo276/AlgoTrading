import yfinance as yf
import pandas as pd

# Define the S&P 500 Index symbol and date range
ticker = '^GSPC'  # S&P 500 Index symbol on Yahoo Finance
start_date = '2017-01-01'
end_date = '2020-12-31'

# Download the historical data
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the percentage change in closing price
data['Close_pct_change'] = data['Close'].pct_change() * 100

# Filter for days where the close price is 1.5% higher than the previous day
filtered_data = data[data['Close_pct_change'] > 1.5]

# Display the result
result = filtered_data[['Close', 'Close_pct_change']]
print(result)
count_days = len(filtered_data)
print("\nNumber of days with more than 1.5% increase:", count_days)