import yfinance as yf
# yFinance is not available in conda channels
# pip install yfinance
# Using pip to install Python packages within a Conda environment
# used as a fallback when the package is not available in Conda's channels.

# import datetime
from datetime import datetime, timedelta, date
import calendar

def get_weeks(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    # Adjust start_date to the first day of the week
    start_date -= timedelta(days=start_date.weekday())

    weeks = []
    current_date = start_date
    week_number = 1

    while current_date <= end_date:
        week_start = current_date
        week_end = current_date + timedelta(days=6)
        weeks.append((week_start, week_end, week_number))
        current_date += timedelta(days=7)
        week_number += 1

    return weeks

def get_month_start_end_dates(year):
    month_dates = []
    for month in range(1, 13):  # Month is 1-based in datetime
        last_day = calendar.monthrange(year, month)[1]
        start_date = date(year, month, 1)
        end_date = date(year, month, last_day)
        month_dates.append((start_date, end_date))
    return month_dates

if __name__ == '__main__':
    year = 2021
    # print(get_month_start_end_dates(year))
    weeks = get_weeks(year)
    #
    ticker_symbols = ["SPY"]
    months = get_month_start_end_dates(year)
    for symbol in ticker_symbols:
        print(symbol)

        for month_start, month_end in months:
            ticker = yf.Ticker(symbol)
            historical_data = ticker.history(start=month_start, end=month_end)
            monthly_change = (historical_data['Close'][-1] - historical_data['Close'][0]) / historical_data['Close'][
                0] * 100
            print(f"{month_start}, {month_end}, {round(monthly_change, 2)}")
            # print(f"{month_start}, {month_end}")

        # for week_start, week_end, week_number in weeks:
        #     # print("Week:", week_number)
        #     # print("Week Start:", week_start.date().year, week_start.date().month, week_start.date().day)
        #     # print("Week End:", week_end.date().year, week_end.date().month, week_end.date().day)
        #     # print()
        #     ticker = yf.Ticker(symbol)
        #     historical_data = ticker.history(start=week_start, end=week_end)
        #
        #     # Calculate the weekly change
        #     weekly_change = (historical_data['Close'][-1] - historical_data['Close'][0]) / historical_data['Close'][0] * 100
        #
        #     # print(f"The weekly change of AAPL is {round(weekly_change, 2)}%.")
        #     print(f"{week_start.date()}, {week_end.date()}, {week_number}, {round(weekly_change, 2)}")


