import os
import matplotlib.pyplot as plt
import pandas as pd


def save_bar_chart(summary: pd.DataFrame, output_path: str) -> None:
    """Save bar chart for category totals."""
    plt.figure(figsize=(10, 6))
    summary["total"].plot(kind="bar")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_pie_chart(summary: pd.DataFrame, output_path: str) -> None:
    """Save pie chart for category totals."""
    plt.figure(figsize=(8, 8))
    plt.pie(
        summary["total"],
        labels=summary.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Expense Distribution by Category")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_line_chart(monthly_summary: pd.DataFrame, output_path: str) -> None:
    """Save line chart for monthly expenses."""
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_summary["month"], monthly_summary["total"], marker="o")
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def generate_category_chart(summary: pd.DataFrame, chart_type: str, base_name: str) -> str:
    """Generate category chart and return saved path."""
    charts_dir = os.path.join("output", "charts")
    os.makedirs(charts_dir, exist_ok=True)

    output_path = os.path.join(charts_dir, f"{base_name}_{chart_type}.png")

    if chart_type == "bar":
        save_bar_chart(summary, output_path)
    elif chart_type == "pie":
        save_pie_chart(summary, output_path)

    return output_path


def generate_monthly_chart(monthly_summary: pd.DataFrame, base_name: str) -> str:
    """Generate monthly trend line chart."""
    charts_dir = os.path.join("output", "charts")
    os.makedirs(charts_dir, exist_ok=True)

    output_path = os.path.join(charts_dir, f"{base_name}_monthly_trend.png")
    save_line_chart(monthly_summary, output_path)
    return output_path