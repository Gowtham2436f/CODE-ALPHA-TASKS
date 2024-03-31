import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity, 'price': self.fetch_current_price(symbol)}

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if quantity >= self.stocks[symbol]['quantity']:
                del self.stocks[symbol]
            else:
                self.stocks[symbol]['quantity'] -= quantity

    def fetch_current_price(self, symbol):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'Global Quote' in data:
                return float(data['Global Quote']['05. price'])
        return None

    def get_portfolio_value(self):
        total_value = 0
        for symbol, info in self.stocks.items():
            current_price = self.fetch_current_price(symbol)
            if current_price:
                total_value += current_price * info['quantity']
        return total_value

    def track_performance(self):
        print("Stock Portfolio Performance:")
        print("============================")
        for symbol, info in self.stocks.items():
            current_price = self.fetch_current_price(symbol)
            if current_price:
                current_value = current_price * info['quantity']
                print(f"{symbol}: Quantity - {info['quantity']}, Current Price - ${current_price}, Current Value - ${current_value}")
            else:
                print(f"{symbol}: Error fetching data")

# Example usage:
if __name__ == "__main__":
    api_key = 'A2M3LF1DD8FXVAMC'  # Replace 'YOUR_API_KEY' with your Alpha Vantage API key
    portfolio = StockPortfolio(api_key)

    portfolio.add_stock('AAPL', 10)  # Adding 10 shares of Apple
    portfolio.add_stock('MSFT', 5)   # Adding 5 shares of Microsoft

    portfolio.track_performance()

    portfolio.remove_stock('AAPL', 5)  # Removing 5 shares of Apple

    portfolio.track_performance()
