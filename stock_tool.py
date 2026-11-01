class StockLookup:
    def __init__(self, stocks):
        self.stock = stocks

    def find_price(self, stock_symbol):
        if stock_symbol in self.stock:
            return self.stock[stock_symbol]
        return None

    def find_product(self, text):
        for product in self.stock:
            if product in text.upper():
                return product
        return None

    def count_for(self, product):
        if product in self.stock:
            return self.stock[product]
        return None
