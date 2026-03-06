import sys
import os
import pandas as pd
import argparse

def main():
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

    args = parser.parse_args()

    filename = args.file
    sort_by = args.sort

    # Готовим пути для вывода
    base = os.path.splitext(os.path.basename(filename))[0]
    os.makedirs("output", exist_ok=True)
    output_txt = os.path.join("output", f"{base}_summary.txt")
    output_csv = os.path.join("output", f"{base}_summary.csv")

    # Читаем CSV (ОДИН раз) + обработка ошибок
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: failed to read CSV: {e}")
        sys.exit(1)

    # Нормализуем названия колонок
    df.columns = df.columns.str.strip().str.lower()

    # Проверяем обязательные колонки
    required = {"category", "amount"}
    missing_cols = required - set(df.columns)
    if missing_cols:
        print(f"Error: missing columns {missing_cols}. Found columns: {list(df.columns)}")
        sys.exit(1)

    # Приводим amount к числу и убираем мусор
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    # Если после очистки данных не осталось — сообщаем
    if df.empty:
        print("Error: no valid numeric values in 'amount' after cleaning.")
        sys.exit(1)

    # Считаем метрики
    total = df["amount"].sum()
    average = df["amount"].mean()

    summary = df.groupby("category")["amount"].agg(
        total="sum",
        average="mean",
        transactions="count"
    )
    summary = summary.sort_values(by=sort_by, ascending=False)
    summary["average"] = summary["average"].round(2)

    # TXT отчёт
    with open(output_txt, "w") as f:
        f.write(f"Total expenses: {total}\n")
        f.write(f"Average expense: {average:.2f}\n\n")
        f.write("Category Summary (sorted by total):\n")
        f.write(summary.to_string())
        f.write("\n")

    # CSV отчёт (category как обычная колонка)
    summary.reset_index().to_csv(output_csv, index=False)

    # Вывод в консоль
    print("\nCategory Summary:")
    print(summary.to_string())
    print(f"\nSaved:\n- {output_txt}\n- {output_csv}")


    if __name__ == "__main__":
        main()