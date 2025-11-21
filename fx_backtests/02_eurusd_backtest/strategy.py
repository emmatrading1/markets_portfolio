import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
DATA_FILE = "data/eurusd_data.csv"
RESULTS_DIR = "results"

FAST_MA = 20          # Fast MA period
SLOW_MA = 50          # Slow MA period
ATR_PERIOD = 14       # Volatility lookback on returns
ATR_PERCENTILE = 30   # Trade only when vol > this percentile
# --------------------------------------------------


def load_data(path: str) -> pd.DataFrame:
    """
    Load EUR/USD CSV, clean it, and return a DataFrame with:
    - datetime index
    - numeric Close column
    """
    print(f"\nLoading data from {path}...")

    df = pd.read_csv(path)

    # Use FIRST column as date (usually 'Date')
    first_col = df.columns[0]
    df[first_col] = pd.to_datetime(df[first_col], errors="coerce")
    df = df.dropna(subset=[first_col])
    df = df.set_index(first_col)

    if "Close" not in df.columns:
        raise ValueError(f"CSV does not contain a 'Close' column. Columns: {list(df.columns)}")

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df[["Close"]].dropna()

    print(f"Rows   : {len(df)}")
    if len(df) > 0:
        print(f"Period : {df.index[0]} -> {df.index[-1]}")
    return df


def run_strategy(df: pd.DataFrame) -> pd.DataFrame:
    """Add indicators, trading signals, and returns to the DataFrame."""
    print("\nCalculating indicators & signals...")

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna(subset=["Close"])

    # Moving averages
    df["MA_Fast"] = df["Close"].rolling(window=FAST_MA).mean()
    df["MA_Slow"] = df["Close"].rolling(window=SLOW_MA).mean()

    # Returns & volatility proxy
    df["Returns"] = df["Close"].pct_change()
    df["TR"] = df["Returns"].abs()
    df["ATR"] = df["TR"].rolling(window=ATR_PERIOD).mean()

    df = df.dropna()

    # Volatility filter threshold
    atr_threshold = df["ATR"].quantile(ATR_PERCENTILE / 100.0)

    # Signals: long when Fast MA > Slow MA and vol above threshold
    df["Signal"] = np.where(
        (df["MA_Fast"] > df["MA_Slow"]) & (df["ATR"] > atr_threshold),
        1,
        0,
    )

    # Entries/exits
    df["Position_Change"] = df["Signal"].diff()
    entries = (df["Position_Change"] == 1).sum()
    exits = (df["Position_Change"] == -1).sum()

    print(f"ATR threshold (vol filter): {atr_threshold:.6f}")
    print(f"Entry signals: {entries}")
    print(f"Exit signals : {exits}")

    # Strategy vs market returns
    df["Market_Returns"] = df["Close"].pct_change()
    df["Strategy_Returns"] = df["Signal"].shift(1) * df["Market_Returns"]

    df["Cumulative_Market"] = (1 + df["Market_Returns"]).cumprod()
    df["Cumulative_Strategy"] = (1 + df["Strategy_Returns"]).cumprod()

    return df


def compute_stats(df: pd.DataFrame) -> dict:
    """Compute performance statistics from strategy DataFrame."""
    stats = {}

    stats["total_return"] = (df["Cumulative_Strategy"].iloc[-1] - 1) * 100
    stats["market_return"] = (df["Cumulative_Market"].iloc[-1] - 1) * 100

    if df["Strategy_Returns"].std() > 0:
        stats["sharpe"] = (
            df["Strategy_Returns"].mean()
            / df["Strategy_Returns"].std()
            * np.sqrt(252)
        )
    else:
        stats["sharpe"] = 0.0

    equity = df["Cumulative_Strategy"]
    running_max = equity.cummax()
    drawdown = (equity - running_max) / running_max
    stats["max_drawdown"] = drawdown.min() * 100

    winning_days = (df["Strategy_Returns"] > 0).sum()
    trading_days = (df["Strategy_Returns"] != 0).sum()
    stats["trading_days"] = trading_days
    stats["win_rate"] = (winning_days / trading_days * 100) if trading_days else 0.0

    stats["total_trades"] = (df["Position_Change"] == 1).sum()

    return stats


def plot_equity(df: pd.DataFrame, out_path: str) -> None:
    """Save equity curve plot."""
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Cumulative_Market"], label="Buy & Hold")
    plt.plot(df.index, df["Cumulative_Strategy"], label="Strategy")
    plt.title("EUR/USD – Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Equity (start = 1.0)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main():
    print("=" * 70)
    print("EUR/USD MOVING AVERAGE CROSSOVER STRATEGY")
    print("=" * 70)

    os.makedirs(RESULTS_DIR, exist_ok=True)

    df = load_data(DATA_FILE)
    if df.empty:
        print("No data after cleaning. Check CSV.")
        return

    df = run_strategy(df)
    stats = compute_stats(df)

    print("\n" + "=" * 70)
    print("PERFORMANCE RESULTS")
    print("=" * 70)

    print(f"\nStrategy Performance:")
    print(f"  Total Return      : {stats['total_return']:>8.2f}%")
    print(f"  Sharpe Ratio      : {stats['sharpe']:>8.2f}")
    print(f"  Max Drawdown      : {stats['max_drawdown']:>8.2f}%")
    print(f"  Win Rate          : {stats['win_rate']:>8.2f}%")

    print(f"\nBenchmark (Buy & Hold):")
    print(f"  Total Return      : {stats['market_return']:>8.2f}%")

    print(f"\nTrading Activity:")
    print(f"  Total Trades      : {stats['total_trades']:>8}")
    print(f"  Days in Market    : {stats['trading_days']:>8}")
    print(f"  Days Out of Market: {len(df) - stats['trading_days']:>8}")

    plot_path = os.path.join(RESULTS_DIR, "eurusd_backtest_equity.png")
    plot_equity(df, plot_path)
    print(f"\nEquity curve saved to: {plot_path}")
    print("\nBacktest complete.")


if __name__ == "__main__":
    main()
