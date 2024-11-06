from datetime import datetime, timedelta
import yfinance as yf
def get_large_positive_open_close_movements(symbol, start_date, end_date, threshold=2.0):
    ticker = yf.Ticker(symbol)
    historical_data = ticker.history(start=start_date, end=end_date)

    # Calculate percentage difference between open and close
    historical_data['Open_Close_Change'] = ((historical_data['Close'] - historical_data['Open']) / historical_data['Open']) * 100

    # Filter dates with a positive open/close difference greater than threshold percentage
    large_movements = historical_data[historical_data['Open_Close_Change'] > threshold]

    return large_movements[['Open', 'Close', 'Open_Close_Change']]

if __name__ == '__main__':
    symbol = "^GSPC"  # Ticker for the S&P 500 index (SPX)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=20 * 365)  # Approx 20 years back

    large_movements = get_large_positive_open_close_movements(symbol, start_date, end_date)
    print(f"Dates with open/close price increase > 1.5% in the past 20 years for {symbol}:\n")
    print(large_movements)