import os
import yfinance as yf
import pandas as pd

# ---------------- CONFIG ----------------
# Yahoo Finance ticker for EUR/USD
TICKER = "EURUSD=X"
START_DATE = "2020-01-01"
END_DATE = "2025-10-20"
DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "eurusd_data.csv")
# ----------------------------------------


def main():
    # Create data/ folder if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    print("Downloading EUR/USD...")
    print(f"Ticker : {TICKER}")
    print(f"Period : {START_DATE} -> {END_DATE}\n")

    try:
        # Download data
        df = yf.download(
            TICKER,
            start=START_DATE,
            end=END_DATE,
            progress=False,
        )

        if df is None or df.empty:
            print("❌ Error: no data downloaded. Check internet connection or ticker.")
            return

        # Keep only the main price columns (optional)
        df = df[["Close", "High", "Low"]]
        df.index.name = "Date"

        # Save to CSV
        df.to_csv(CSV_PATH)

        print("✅ Download successful")
        print(f"Rows       : {len(df)}")
        print(f"Date range : {df.index[0].date()} -> {df.index[-1].date()}")
        print(f"Saved to   : {CSV_PATH}\n")

        print("First 5 rows:")
        print(df.head())

    except Exception as e:
        print(f"\n❌ FX Error: {e}")
        print("Make sure libs are installed:  pip install yfinance pandas numpy")


if __name__ == "__main__":
    main()
