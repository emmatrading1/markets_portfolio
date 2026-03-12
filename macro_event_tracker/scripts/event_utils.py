import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "events_log.csv"


def load_events(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def compute_surprise(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["previous", "consensus", "actual"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["surprise"] = df["actual"] - df["consensus"]
    return df


def upcoming_events(df: pd.DataFrame, country: str | None = None) -> pd.DataFrame:
    df = df.copy()
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"], errors="coerce")

    if country:
        df = df[df["country"] == country]

    return df.sort_values("datetime")


def filter_by_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    return df[df["category"].str.lower() == category.lower()].copy()


if __name__ == "__main__":
    events = load_events()
    events = compute_surprise(events)
    print(events.head())

def biggest_surprises(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    df = df.copy()
    df["abs_surprise"] = df["surprise"].abs()
    return df.sort_values("abs_surprise", ascending=False).head(n)

import pandas as pd

def biggest_surprises(df: pd.DataFrame, n: int = 5):
    df = df.copy()
    df["abs_surprise"] = df["surprise"].abs()
    return df.sort_values("abs_surprise", ascending=False).head(n)

def reaction_by_asset(df: pd.DataFrame, asset: str):
    return df[df["asset"] == asset][
        ["date", "event", "surprise", "move"]
    ]

def macro_shock_score(df):
    df = df.copy()

    df["abs_surprise"] = df["surprise"].abs()

    return df.sort_values("abs_surprise", ascending=False)

def top_macro_shocks(df, n=3):

    ranked = macro_shock_score(df)

    return ranked.head(n)[
        ["date", "country", "event", "surprise", "market_reaction"]
    ]

def inflation_shock_indicator(df):

    inflation_events = df[df["category"] == "inflation"]

    avg_surprise = inflation_events["surprise"].mean()

    if avg_surprise > 0:
        return "Inflation running HOT"
    elif avg_surprise < 0:
        return "Inflation running COOL"
    else:
        return "Inflation neutral"