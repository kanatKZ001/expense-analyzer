import pandas as pd


def save_summary_csv(path, summary):

    df = summary.reset_index().copy()

    df.insert(0, "rank", range(1, len(df) + 1))

    total = df["total"].sum()

    df["share_percent"] = (df["total"] / total * 100).round(2)

    df = df.rename(columns={
        "total": "total_amount",
        "average": "average_amount",
        "transactions": "transactions_count"
    })

    df = df[
        [
            "rank",
            "category",
            "total_amount",
            "average_amount",
            "transactions_count",
            "share_percent",
        ]
    ]

    df.to_csv(path, index=False)


def save_monthly_csv(path, monthly):

    df = monthly.copy()

    df.insert(0, "rank", range(1, len(df) + 1))

    df = df.rename(columns={
        "total": "total_amount"
    })

    df = df[
        [
            "rank",
            "month",
            "total_amount"
        ]
    ]

    df.to_csv(path, index=False)