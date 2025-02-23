import csv
from datetime import datetime

# Global portfolio list to store all investments
portfolio = []


def display_menu():
    """
    Display the main menu options.
    """
    print("\nInvestment Portfolio Tracker")
    print("1. Add Investment")
    print("2. Update Investment")
    print("3. Remove Investment")
    print("4. Display Portfolio")
    print("5. Portfolio Summary")
    print("0. Exit")


def add_investment():
    """
    Add a new investment to the portfolio.

    Prompts the user for investment details and appends the investment as a dictionary
    to the global portfolio list.
    """
    print("\nAdd New Investment")
    ticker = input("Enter the ticker symbol: ").upper()
    try:
        purchase_price = float(input("Enter the purchase price: "))
        current_price = float(input("Enter the current price: "))
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Invalid input for price or quantity. Please enter numeric values.")
        return

    purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")
    # Validate the date format
    try:
        datetime.strptime(purchase_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    investment = {
        "ticker": ticker,
        "purchase_price": purchase_price,
        "current_price": current_price,
        "quantity": quantity,
        "purchase_date": purchase_date
    }
    portfolio.append(investment)
    print(f"Added investment: {ticker}")


def update_investment():
    """
    Update an existing investment in the portfolio.

    Searches for an investment by its ticker symbol and allows the user to update its details.
    """
    print("\nUpdate Investment")
    ticker = input("Enter the ticker symbol of the investment to update: ").upper()
    found = False
    for inv in portfolio:
        if inv["ticker"] == ticker:
            found = True
            print(f"Current details: {inv}")
            try:
                new_purchase_price = input("Enter new purchase price (or press Enter to skip): ")
                new_purchase_price = float(new_purchase_price) if new_purchase_price else inv["purchase_price"]
                new_current_price = input("Enter new current price (or press Enter to skip): ")
                new_current_price = float(new_current_price) if new_current_price else inv["current_price"]
                new_quantity = input("Enter new quantity (or press Enter to skip): ")
                new_quantity = int(new_quantity) if new_quantity else inv["quantity"]
            except ValueError:
                print("Invalid input. Update aborted.")
                return

            new_purchase_date = input("Enter new purchase date (YYYY-MM-DD) (or press Enter to skip): ") or inv[
                "purchase_date"]
            if new_purchase_date != inv["purchase_date"]:
                try:
                    datetime.strptime(new_purchase_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Update aborted.")
                    return

            inv["purchase_price"] = new_purchase_price
            inv["current_price"] = new_current_price
            inv["quantity"] = new_quantity
            inv["purchase_date"] = new_purchase_date
            print("Investment updated successfully.")
            break
    if not found:
        print("Investment not found.")


def remove_investment():
    """
    Remove an investment from the portfolio.

    Searches for an investment by ticker symbol and removes it if found.
    """
    print("\nRemove Investment")
    ticker = input("Enter the ticker symbol of the investment to remove: ").upper()
    global portfolio
    new_portfolio = [inv for inv in portfolio if inv["ticker"] != ticker]
    if len(new_portfolio) == len(portfolio):
        print("Investment not found.")
    else:
        portfolio[:] = new_portfolio
        print(f"Investment {ticker} removed.")


def display_portfolio():
    """
    Display all investments in the portfolio.

    Iterates through the portfolio list and prints details of each investment.
    """
    print("\nYour Investment Portfolio:")
    if not portfolio:
        print("Portfolio is empty.")
        return
    for inv in portfolio:
        print(f"Ticker: {inv['ticker']}, Purchase Price: {inv['purchase_price']}, "
              f"Current Price: {inv['current_price']}, Quantity: {inv['quantity']}, "
              f"Purchase Date: {inv['purchase_date']}")

def calculate_portfolio_summary():
    """
    Calculate and display a summary of the portfolio, including total value and total profit/loss.

    Profit/loss is calculated as (current_price - purchase_price) * quantity for each investment.
    """
    if not portfolio:
        print("Portfolio is empty.")
        return
    total_value = 0.0
    total_profit_loss = 0.0
    for inv in portfolio:
        investment_value = inv["current_price"] * inv["quantity"]
        profit_loss = (inv["current_price"] - inv["purchase_price"]) * inv["quantity"]
        total_value += investment_value
        total_profit_loss += profit_loss
    print("\nPortfolio Summary:")
    print(f"Total Portfolio Value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit_loss:.2f}")

def main():
    """
    Main function to run the Investment Portfolio Tracker.

    Provides a menu-driven interface for managing investments.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_investment()
        elif choice == "2":
            update_investment()
        elif choice == "3":
            remove_investment()
        elif choice == "4":
            display_portfolio()
        elif choice == "5":
            calculate_portfolio_summary()
        elif choice == "0":
            print("Exiting Investment Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
