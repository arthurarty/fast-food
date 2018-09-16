class Order:
    """Class Order represents an order placed by a customer"""

    def __init__(self, customer_name, item_name, quantity):
        """initiate an instance of class Order"""
        self.customer_name = customer_name
        self.item_name = item_name
        self.quantity = quantity

    def get_customer_name(self):
        """method returns customer name"""
        return self.customer_name

    def get_item_name(self):
        """method returns item name"""
        return self.item_name
