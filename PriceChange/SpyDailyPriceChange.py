from datetime import datetime, timedelta
import yfinance as yf

def get_large_consecutive_close_movements(symbol, start_date, end_date, threshold=1.5):
    ticker = yf.Ticker(symbol)
    historical_data = ticker.history(start=start_date, end=end_date)

    # Calculate the percentage change from the previous day's close to today's close
    historical_data['Close_Close_Change'] = historical_data['Close'].pct_change() * 100

    # Filter days where the close-to-close difference is greater than the threshold
    large_movements = historical_data[historical_data['Close_Close_Change'] > threshold]

    return large_movements[['Close', 'Close_Close_Change']]

if __name__ == '__main__':
    symbol = "^GSPC"  # Ticker for the S&P 500 index (SPX)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=20 * 365)  # Approx 20 years back

    large_movements = get_large_consecutive_close_movements(symbol, start_date, end_date)
    print(f"Dates with previous close to current close increase > 1.5% in the past 20 years for {symbol}:\n")
    print(large_movements)