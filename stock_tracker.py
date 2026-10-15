"""
Stock Portfolio Tracker
-----------------------
Calculates total investment value from user-entered stock names and quantities,
using a hardcoded dictionary of stock prices. Optionally saves the result to
a .txt or .csv file.

Key concepts: dictionary, input/output, basic arithmetic, file handling.
"""

import csv

# Hardcoded stock prices (USD per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def show_available_stocks():
    """Print the list of stocks the tracker knows about."""
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price:>8,.2f}")
    print()


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a list of holdings."""
    portfolio = []
    print("Enter your stocks one at a time. Type 'done' when finished.\n")

    while True:
        name = input("Stock name (or 'done'): ").strip().upper()

        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print(f"  '{name}' not found. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        try:
            quantity = int(qty_text)
        except ValueError:
            print("  Please enter a whole number for quantity.")
            continue
        if quantity <= 0:
            print("  Quantity must be greater than zero.")
            continue

        price = STOCK_PRICES[name]
        portfolio.append({
            "stock": name,
            "quantity": quantity,
            "price": price,
            "value": price * quantity,
        })
        print(f"  Added {quantity} x {name} @ ${price:,.2f}\n")

    return portfolio


def calculate_total(portfolio):
    """Return the total investment value of the portfolio."""
    return sum(item["value"] for item in portfolio)


def display_portfolio(portfolio, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 46)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Value':>16}")
    print("-" * 46)
    for item in portfolio:
        print(f"{item['stock']:<8}{item['quantity']:>6}"
              f"{item['price']:>12,.2f}{item['value']:>16,.2f}")
    print("-" * 46)
    print(f"{'TOTAL INVESTMENT':<26}{total:>20,.2f}")
    print("=" * 46)


def save_to_txt(portfolio, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 30 + "\n")
        for item in portfolio:
            f.write(f"{item['stock']}: {item['quantity']} x "
                    f"${item['price']:,.2f} = ${item['value']:,.2f}\n")
        f.write("=" * 30 + "\n")
        f.write(f"Total Investment: ${total:,.2f}\n")


def save_to_csv(portfolio, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for item in portfolio:
            writer.writerow([item["stock"], item["quantity"],
                             item["price"], item["value"]])
        writer.writerow(["TOTAL", "", "", total])


def ask_to_save(portfolio, total):
    """Offer to save results to a file."""
    choice = input("\nSave result to a file? (txt / csv / no): ").strip().lower()
    try:
        if choice == "txt":
            save_to_txt(portfolio, total)
            print("Saved to portfolio.txt")
        elif choice == "csv":
            save_to_csv(portfolio, total)
            print("Saved to portfolio.csv")
        else:
            print("Not saved.")
    except OSError as err:
        print(f"Could not save file: {err}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio()
    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    total = calculate_total(portfolio)
    display_portfolio(portfolio, total)
    ask_to_save(portfolio, total)


if __name__ == "__main__":
    main()
