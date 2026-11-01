# Author: James Rhodes


class OrderLookup:
    def __init__(self, orders):
        self.orders = orders

    def find_order_id(self, text):
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id
        return None

    def find_status(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]
        return None
