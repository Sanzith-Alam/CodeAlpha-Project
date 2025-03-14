import requests

# Replace with your Alpha Vantage API key
API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary to store stocks: {symbol: shares}

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio."""
        if symbol.upper() in self.portfolio:
            print(f"{symbol.upper()} is already in your portfolio. Updating shares.")
            self.portfolio[symbol.upper()] += shares
        else:
            self.portfolio[symbol.upper()] = shares
            print(f"Added {shares} shares of {symbol.upper()} to your portfolio.")

    def remove_stock(self, symbol):
        """Remove a stock from the portfolio."""
        if symbol.upper() in self.portfolio:
            del self.portfolio[symbol.upper()]
            print(f"Removed {symbol.upper()} from your portfolio.")
        else:
            print(f"{symbol.upper()} is not in your portfolio.")

    def get_stock_price(self, symbol):
        """Fetch the current stock price using Alpha Vantage API."""
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if 'Global Quote' in data:
            return float(data['Global Quote']['05. price'])
        else:
            print(f"Error fetching data for {symbol}. Please check the symbol or try again later.")
            return None

    def view_portfolio(self):
        """Display the current portfolio and its total value."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        total_value = 0
        print("\nYour Portfolio:")
        print("-" * 30)
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                value = price * shares
                total_value += value
                print(f"{symbol}: {shares} shares | Price: ${price:.2f} | Value: ${value:.2f}")
        print("-" * 30)
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter the stock symbol (e.g., AAPL): ").strip().upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter the stock symbol to remove: ").strip().upper()
            portfolio.remove_stock(symbol)
        elif choice == '3':
            portfolio.view_portfolio()
        elif choice == '4':
            print("Exiting the Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()