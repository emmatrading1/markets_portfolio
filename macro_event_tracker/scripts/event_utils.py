from pathlib import Path
import pandas as pd


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "events_log.csv"


def load_events(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def compute_surprise(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["previous", "forecast", "actual"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "actual" in df.columns and "forecast" in df.columns:
        df["surprise"] = df["actual"] - df["forecast"]

    return df


def upcoming_events(df: pd.DataFrame, country: str | None = None) -> pd.DataFrame:
    df = df.copy()

    if "time" in df.columns:
        df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"], errors="coerce")
    else:
        df["datetime"] = pd.to_datetime(df["date"], errors="coerce")

    if country:
        df = df[df["country"] == country]

    return df.sort_values("datetime")


def filter_by_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    df = df.copy()
    return df[df["category"].str.lower() == category.lower()]


def biggest_surprises(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    df = df.copy()
    df["abs_surprise"] = df["surprise"].abs()
    return df.sort_values("abs_surprise", ascending=False).head(n)


def reaction_by_asset(df: pd.DataFrame, asset: str) -> pd.DataFrame:
    df = df.copy()

    if "asset" not in df.columns or "move" not in df.columns:
        raise ValueError("The dataframe must contain 'asset' and 'move' columns.")

    return df[df["asset"] == asset][["date", "event", "surprise", "move"]]


def macro_shock_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["abs_surprise"] = df["surprise"].abs()
    return df.sort_values("abs_surprise", ascending=False)


def top_macro_shocks(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    grouped = (
        df.groupby(["date", "country", "event", "category"], as_index=False)
        .agg(
            surprise=("surprise", "first"),
            notes=("notes", "first")
        )
    )

    grouped["abs_surprise"] = grouped["surprise"].abs()

    return grouped.sort_values("abs_surprise", ascending=False).head(n)


def inflation_shock_indicator(df: pd.DataFrame) -> str:
    df = df.copy()

    inflation_events = df[df["category"].str.lower() == "inflation"]

    if inflation_events.empty:
        return "No inflation events in dataset"

    avg_surprise = inflation_events["surprise"].mean()

    if avg_surprise > 0:
        return "Inflation running HOT"
    elif avg_surprise < 0:
        return "Inflation running COOL"
    else:
        return "Inflation neutral"


if __name__ == "__main__":
    events = load_events()
    events = compute_surprise(events)
    print(events.head())