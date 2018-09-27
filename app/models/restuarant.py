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

    def get_single_order(self, id):
        """return a specific order"""
        if id > len(self.orders):
            return False
        index = id - 1
        return self.orders[index]

    def update_order_status(self, id, status):
        """update the status of an order"""
        if id > len(self.orders):
            return False
        index = id - 1

        self.orders[index]['status'] = status
        return self.orders[index]
