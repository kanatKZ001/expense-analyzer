# Expense Analyzer CLI

A simple command-line tool for analyzing expenses from a CSV file using Python and pandas.

The program calculates:

- Total expenses
- Average expense
- Expenses grouped by category
- Number of transactions per category

Results are saved as:

- `.txt` report
- `.csv` summary file

---

# Features

- CLI interface
- CSV parsing with pandas
- Data cleaning (handles invalid numbers)
- Automatic output folder creation
- Category statistics
- Sorted results by total expenses

---

# Installation

Clone the repository:

```bash
git clone https://github.com/kanatkZ001/expense-analyzer.git
cd expense-analyzer
Install dependencies:
pip install -r requirements.txt

---

# Usage

Run the program with a CSV file:
python main.py sample_data/expenses.csv

Example CSV format:

category,amount
food,1200
books,3000
transport,700
food,2400
transport,700

Optional arguments:

--sort total
--sort average
--sort transactions

---

#  Example Output

Terminal output:
Total expenses: 8000
Average expense: 1333.33

Category Summary:
category   total   average   transactions
food       3600    1200      3
books      3000    3000      1
transport  1400    700       2

Generated files:

output/
 ├── expenses_summary.txt
 └── expenses_summary.csv
 
---

#  Project Structure

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

---

# Technologies Used
Python
pandas
CLI tools
Git / GitHub

---

# Future Improvements
charts and visualizations
monthly analysis
support for multiple currencies
interactive CLI arguments

---

# Author
Kanat Zhumatov

Computer Science student interested in data science, machine learning and finance.