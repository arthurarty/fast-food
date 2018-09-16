class Restuarant:
    """a restuarant has several orders stored in a list """

    def __init__(self):
        """initate an instance of class resturant"""
        self.orders = {}

    def add_order(self, order):
        """add a new order """
        no_of_orders = len(self.orders) + 1
        self.orders[no_of_orders] = order.__dict__
        return self.orders

    def get_orders(self):
        """return all orders"""
        return self.orders
