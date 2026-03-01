# Expense Analyzer (Python)

A simple CLI tool to analyze expenses from a CSV file and generate summary reports.

## Input CSV format
The CSV should contain at least these columns:
- `category`
- `amount`

Example:

category,amount  
food,1200  
transport,700  

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt