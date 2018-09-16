class Restuarant:
    """a restuarant has several orders stored in a list """

    def __init__(self):
        """initate an instance of class resturant"""
        self.orders = []

    def add_order(self, order):
        """add a new order """
        self.orders.append(order.__dict__)
        return self.orders

    def get_orders(self):
        """return all orders"""
        return self.orders
