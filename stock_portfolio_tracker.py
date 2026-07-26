"""
Task 2: Stock Portfolio Tracker
------------------------------------------
Calculates the total value of a portfolio based on hardcoded stock
prices, and allows saving the result as .txt or .csv.
"""

import csv

# Hardcoded dictionary: prices of available stocks
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420,
}


def show_available_stocks():
    print("\nAvailable stocks and their prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"  - {stock}: ${price}")
    print()


def input_portfolio():
    """Asks the user to enter their stocks and quantities."""
    portfolio = {}

    print("Enter a stock name and its quantity.")
    print("Type 'done' as the stock name to finish.\n")

    while True:
        name = input("Stock name (e.g. AAPL): ").strip().upper()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print(f"⚠️  '{name}' is not recognized. Valid stocks: {', '.join(STOCK_PRICES.keys())}\n")
            continue

        try:
            quantity = int(input(f"Quantity of {name}: ").strip())
            if quantity < 0:
                print("⚠️  Quantity must be positive.\n")
                continue
        except ValueError:
            print("⚠️  Please enter a valid whole number.\n")
            continue

        # If the stock is already present, add up the quantities
        portfolio[name] = portfolio.get(name, 0) + quantity
        print(f"✅ {quantity} share(s) of {name} added.\n")

    return portfolio


def calculate_total_value(portfolio):
    """Calculates the total investment value and the breakdown per stock."""
    breakdown = []
    total = 0

    for stock, quantity in portfolio.items():
        unit_price = STOCK_PRICES[stock]
        value = quantity * unit_price
        total += value
        breakdown.append((stock, quantity, unit_price, value))

    return breakdown, total


def show_result(breakdown, total):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<10}{'Quantity':<12}{'Unit Price':<12}{'Value':<10}")
    print("-" * 45)
    for stock, quantity, unit_price, value in breakdown:
        print(f"{stock:<10}{quantity:<12}{unit_price:<12}{value:<10}")
    print("-" * 45)
    print(f"TOTAL INVESTMENT VALUE: ${total}")
    print("=" * 45 + "\n")


def save_txt(breakdown, total, path="portfolio.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("PORTFOLIO SUMMARY\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Stock':<10}{'Quantity':<12}{'Unit Price':<12}{'Value':<10}\n")
        f.write("-" * 45 + "\n")
        for stock, quantity, unit_price, value in breakdown:
            f.write(f"{stock:<10}{quantity:<12}{unit_price:<12}{value:<10}\n")
        f.write("-" * 45 + "\n")
        f.write(f"TOTAL INVESTMENT VALUE: ${total}\n")
    print(f"💾 Result saved to '{path}'")


def save_csv(breakdown, total, path="portfolio.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Unit Price", "Value"])
        for stock, quantity, unit_price, value in breakdown:
            writer.writerow([stock, quantity, unit_price, value])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", total])
    print(f"💾 Result saved to '{path}'")


def offer_save(breakdown, total):
    choice = input("Would you like to save the result? (txt / csv / no): ").strip().lower()

    if choice == "txt":
        save_txt(breakdown, total)
    elif choice == "csv":
        save_csv(breakdown, total)
    else:
        print("No file saved.")


def main():
    print("📈 STOCK PORTFOLIO TRACKER")
    show_available_stocks()

    portfolio = input_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting program.")
        return

    breakdown, total = calculate_total_value(portfolio)
    show_result(breakdown, total)
    offer_save(breakdown, total)


if __name__ == "__main__":
    main()
