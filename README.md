# Expense Analyzer CLI

A Python command-line tool for analyzing and visualizing expenses from CSV files.

This project demonstrates **data cleaning, aggregation, visualization, and report generation using Python and pandas**.
It can generate summaries, filter transactions, and create charts for expense analysis.

---

## Features

* Analyze expenses from CSV files
* Clean and validate financial data
* Group expenses by category
* Calculate totals, averages, and transaction counts
* Generate professional CSV reports
* Create visual charts:

  * Category bar chart
  * Category pie chart
  * Monthly expense trend
* Filter expenses by:

  * category
  * minimum amount
  * month
* Command-line interface for flexible analysis

---

## Project Structure

```
expense-analyzer
│
├── main.py              # CLI entry point
├── analyzer.py          # Data processing logic
├── export.py            # Report generation
├── visualization.py     # Charts and graphs
│
├── sample_data
│   └── expenses.csv
│
├── output
│   └── charts
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/expense-analyzer.git
cd expense-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Example Dataset

Example CSV format:

```
date,category,amount
2026-01-05,Food,120
2026-01-07,Transport,45
2026-01-10,Books,320
2026-01-15,Food,230
```

---

## Usage

Basic analysis:

```
python main.py sample_data/expenses.csv
```

Sort categories by average:

```
python main.py sample_data/expenses.csv --sort average
```

Show top 5 categories:

```
python main.py sample_data/expenses.csv --top 5
```

Filter by category:

```
python main.py sample_data/expenses.csv --category Food
```

Filter by month:

```
python main.py sample_data/expenses.csv --month 2026-02
```

Generate category chart:

```
python main.py sample_data/expenses.csv --chart bar
```

Generate monthly trend chart:

```
python main.py sample_data/expenses.csv --monthly-chart
```

---

## Output

The tool generates reports inside the `output` folder:

```
output/
├── expenses_summary.txt
├── expenses_summary.csv
├── expenses_monthly_summary.csv
└── charts/
    ├── expenses_bar.png
    ├── expenses_pie.png
    └── expenses_monthly_trend.png
```

Example CSV report:

```
rank,category,total_amount,average_amount,transactions_count,share_percent
1,Rent,7200.00,1200.00,6,38.14
2,Food,2735.00,227.92,12,14.50
3,Shopping,2710.00,451.67,6,14.37
```

---

## Technologies Used

* Python
* pandas
* matplotlib
* argparse

---

## Possible Improvements

Future enhancements could include:

* interactive dashboards (Streamlit)
* export to Excel reports
* automated data pipelines
* web interface

---

## Author

Kanat Zhumatov

Computer Science student interested in **data analysis, automation, and Python tools**.

---
