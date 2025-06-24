import yfinance as yf # type: ignore
import pandas as pd
import numpy as np
import sys

def download_stock_data(ticker, period, output_filename):
    data = yf.download(ticker, period=period)
    # Remove unnecessary columns
    data = data[[('Close', ticker), ('High', ticker)]]
    # Calculate daily return
    data['Return'] = data[('Close', ticker)].pct_change()

    # Round the values to 3 decimal places
    data[('Close', ticker)] = data[('Close', ticker)].round(3)
    data[('High', ticker)] = data[('High', ticker)].round(3)
    data['Return'] = data['Return'].round(3)

    data.to_csv(output_filename, float_format='%.3f')

if __name__ == "__main__":
    ticker = sys.argv[1]
    period = sys.argv[2]
    output_dir = sys.argv[3]
    output_filename = f"{output_dir}/{ticker}_stock_data.csv"
    download_stock_data(ticker, period, output_filename)