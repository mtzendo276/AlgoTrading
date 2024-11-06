import yfinance as yf
import pandas as pd

# Define the S&P 500 Index symbol, date range, and percentage threshold
ticker = '^GSPC'  # S&P 500 Index symbol on Yahoo Finance
start_date = '2000-01-01'
end_date = '2024-10-31'
threshold = 3.0  # Define the percentage threshold

# Download the historical data
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the percentage change in closing price
data['Close_pct_change'] = data['Close'].pct_change() * 100

# Add the previous day's close price
data['Previous_Close'] = data['Close'].shift(1)

# Calculate the price difference
data['Price_Difference'] = data['Close'] - data['Previous_Close']

# Filter for days where the close price is higher than the threshold percentage
filtered_data = data[data['Close_pct_change'] > threshold]

# Count the number of days
count_days = len(filtered_data)

# Set option to display all rows
pd.set_option('display.max_rows', None)

# Display the result with previous day's close, current close, percentage change, and price difference
result = filtered_data[['Previous_Close', 'Close', 'Price_Difference', 'Close_pct_change']]
print(result)
print(f"\nNumber of days with more than {threshold}% increase:", count_days)

# Reset the display option if needed
pd.reset_option('display.max_rows')