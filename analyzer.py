import pandas as pd
import sys


def load_data(filename: str) -> pd.DataFrame:
    """Load CSV file."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower()
    return df


def validate_columns(df: pd.DataFrame):
    required = {"category", "amount"}
    missing = required - set(df.columns)

    if missing:
        print(f"Missing columns: {missing}")
        sys.exit(1)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df["category"] = df["category"].astype(str).str.strip()

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

    if df.empty:
        print("No valid data after cleaning")
        sys.exit(1)

    return df


def apply_filters(df, min_amount=None, category=None, month=None):

    if min_amount is not None:
        df = df[df["amount"] >= min_amount]

    if category:
        df = df[df["category"].str.lower() == category.lower()]

    if month:

        if "date" not in df.columns:
            print("Month filter requires date column")
            sys.exit(1)

        df = df[df["date"].dt.strftime("%Y-%m") == month]

    if df.empty:
        print("No data matched filters")
        sys.exit(1)

    return df


def build_category_summary(df, sort_by):

    summary = df.groupby("category")["amount"].agg(
        total="sum",
        average="mean",
        transactions="count"
    )

    summary["total"] = summary["total"].round(2)
    summary["average"] = summary["average"].round(2)

    return summary.sort_values(by=sort_by, ascending=False)


def build_monthly_summary(df):

    if "date" not in df.columns:
        return None

    monthly = df.copy()

    monthly["month"] = monthly["date"].dt.strftime("%Y-%m")

    monthly_summary = (
        monthly.groupby("month")["amount"]
        .sum()
        .reset_index(name="total")
        .sort_values("month")
    )

    monthly_summary["total"] = monthly_summary["total"].round(2)

    return monthly_summary