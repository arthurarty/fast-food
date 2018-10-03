"""the food class"""
class Food():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

