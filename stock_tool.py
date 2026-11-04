class StockLookup:
    def __init__(self, stock_data):
        self.stock = stock_data
        self.items = list(stock_data.keys())

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

    def find_item(self, user_message):
        text = user_message.lower()
        for item in self.items:
            if item.lower() in text:
                return item
        return None

    def get_stock(self, item):
        return self.stock.get(item)
