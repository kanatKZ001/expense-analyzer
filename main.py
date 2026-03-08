import os
import sys
import argparse
import pandas as pd

from analyzer import (
    load_data,
    normalize_columns,
    validate_columns,
    clean_data,
    apply_filters,
    build_category_summary,
    build_monthly_summary,
)

from export import (
    save_summary_csv,
    save_monthly_csv,
)

from visualization import (
    generate_category_chart,
    generate_monthly_chart,
)


def save_report_txt(
    output_txt: str,
    total: float,
    average: float,
    sort_by: str,
    summary,
    monthly_summary=None
) -> None:
    """Save text report."""
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(f"Total expenses: {total:.2f}\n")
        f.write(f"Average expense: {average:.2f}\n\n")
        f.write(f"Category Summary (sorted by {sort_by}):\n")
        f.write(summary.to_string())
        f.write("\n")

        if monthly_summary is not None and not monthly_summary.empty:
            f.write("\nMonthly Summary:\n")
            f.write(monthly_summary.to_string(index=False))
            f.write("\n")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Expense Analyzer CLI")

    parser.add_argument(
        "file",
        help="Path to CSV file with expenses"
    )

    parser.add_argument(
        "--sort",
        choices=["total", "average", "transactions"],
        default="total",
        help="Sort category summary by selected column"
    )

    parser.add_argument(
        "--top",
        type=int,
        help="Show only top N categories"
    )

    parser.add_argument(
        "--min-amount",
        type=float,
        help="Filter transactions with amount >= this value"
    )

    parser.add_argument(
        "--category",
        type=str,
        help="Filter by category name"
    )

    parser.add_argument(
        "--month",
        type=str,
        help="Filter by month in format YYYY-MM"
    )

    parser.add_argument(
        "--chart",
        choices=["bar", "pie"],
        help="Generate category chart"
    )

    parser.add_argument(
        "--monthly-chart",
        action="store_true",
        help="Generate monthly trend chart"
    )

    return parser.parse_args()


def validate_arguments(args):
    if args.top is not None and args.top <= 0:
        print("Error: --top must be greater than 0.")
        sys.exit(1)

    if args.month is not None:
        try:
            pd.to_datetime(args.month, format="%Y-%m")
        except ValueError:
            print("Error: --month must be in format YYYY-MM.")
            sys.exit(1)


def prepare_output_paths(filename: str):
    base = os.path.splitext(os.path.basename(filename))[0]
    os.makedirs("output", exist_ok=True)

    output_txt = os.path.join("output", f"{base}_summary.txt")
    output_csv = os.path.join("output", f"{base}_summary.csv")
    output_monthly_csv = os.path.join("output", f"{base}_monthly_summary.csv")

    return base, output_txt, output_csv, output_monthly_csv


def print_results(summary, monthly_summary, output_txt, output_csv, output_monthly_csv=None):
    print("\nCategory Summary:")
    print(summary.to_string())

    if monthly_summary is not None and not monthly_summary.empty:
        print("\nMonthly Summary:")
        print(monthly_summary.to_string(index=False))

    print(f"\nSaved:\n- {output_txt}\n- {output_csv}")

    if output_monthly_csv and monthly_summary is not None and not monthly_summary.empty:
        print(f"- {output_monthly_csv}")


def main():
    args = parse_arguments()
    validate_arguments(args)

    base, output_txt, output_csv, output_monthly_csv = prepare_output_paths(args.file)

    df = load_data(args.file)
    df = normalize_columns(df)
    validate_columns(df)
    df = clean_data(df)
    df = apply_filters(
        df,
        min_amount=args.min_amount,
        category=args.category,
        month=args.month
    )

    total = df["amount"].sum()
    average = df["amount"].mean()

    summary = build_category_summary(df, args.sort)

    if args.top is not None:
        summary = summary.head(args.top)

    monthly_summary = build_monthly_summary(df)

    save_report_txt(output_txt, total, average, args.sort, summary, monthly_summary)
    save_summary_csv(output_csv, summary)

    if monthly_summary is not None and not monthly_summary.empty:
        save_monthly_csv(output_monthly_csv, monthly_summary)

    print_results(summary, monthly_summary, output_txt, output_csv, output_monthly_csv)

    if args.chart:
        chart_path = generate_category_chart(summary, args.chart, base)
        print(f"- {chart_path}")

    if args.monthly_chart:
        if monthly_summary is None or monthly_summary.empty:
            print("Error: monthly chart requires a valid 'date' column with usable data.")
            sys.exit(1)

        monthly_chart_path = generate_monthly_chart(monthly_summary, base)
        print(f"- {monthly_chart_path}")


if __name__ == "__main__":
    main()