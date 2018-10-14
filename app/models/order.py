"""File contains class order"""
from datetime import datetime


class Order:
    """
    Class Order represents an order placed by a customer
    """

    def __init__(self, menu_id, user_id, quantity):
        """initiate an instance of class Order"""
        self.menu_id = menu_id
        self.user_id = user_id
        self.quantity = quantity
        self.status = 'New'
        self.created_at = datetime.now()
