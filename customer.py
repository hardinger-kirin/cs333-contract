import names # random name generation
import random # random order generation
import order

class Customer():
    def __init__(self):
        self.name = names.get_first_name()

    def get_name(self):
        return self.name
    
    def overrite_name(self, name):
        self.name = name
    
    def generate_order(self, inventory):
        # generate random order
        base = random.choice(inventory.get_bases())
        boba = random.choice(inventory.get_bobas())
        # checks if there are any toppings in the inventory before adding
        # if there are no toppings, then the customer will not order any toppings
        topping = ''
        if inventory.get_length("topping") != 0:
            topping = (random.choice(inventory.get_toppings()))
        return order.Order(base, boba, topping)