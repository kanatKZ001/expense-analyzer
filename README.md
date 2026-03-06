# Expense Analyzer CLI

A simple command-line tool for analyzing expenses from a CSV file using **Python** and **pandas**.

The program processes a CSV file with expenses and calculates useful statistics such as totals, averages, and category summaries.

---

## Features

* CLI interface using `argparse`
* CSV parsing with **pandas**
* Automatic data cleaning (handles invalid numbers)
* Category-based expense analysis
* Sorting results by different metrics
* Automatic creation of output folder
* Generates summary reports in `.txt` and `.csv`

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kanatkZ001/expense-analyzer.git
cd expense-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program with a CSV file:

```bash
python main.py sample_data/expenses.csv
```

### Optional arguments

Sort the category summary by different columns:

```bash
python main.py sample_data/expenses.csv --sort total
python main.py sample_data/expenses.csv --sort average
python main.py sample_data/expenses.csv --sort transactions
```

---

## Example CSV format

```csv
category,amount
food,1200
books,3000
transport,700
food,2400
transport,700
```

---

## Example Output

Terminal output:

```text
Category Summary:

category   total   average   transactions
food       3600    1200.0    3
books      3000    3000.0    1
transport  1400    700.0     2
```

Generated files:

```text
output/
 ├── expenses_summary.txt
 └── expenses_summary.csv
```

---

## Project Structure

```
expense-analyzer
│
├── main.py
├── requirements.txt
├── README.md
│
├── sample_data
│   └── expenses.csv
│
└── output
```

---

## Technologies Used

* Python
* pandas
* argparse
* Git
* GitHub

---

## Future Improvements

Possible improvements for the project:

* expense visualization (charts)
* monthly expense analysis
* multiple currency support
* interactive CLI options
* exporting reports to more formats

---

## Author

Kanat Zhumatov

Computer Science student interested in:

* Data Science
* Machine Learning
* Finance
* Software Development
