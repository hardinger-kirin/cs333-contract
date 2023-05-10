import unittest
from customer import *
from ingredient import *
from inventory import *
from order import *

class TestMethods(unittest.TestCase):
    # UNIT TESTS FOR CUSTOMER CLASS
    def test_get_set_name(self):
        test_customer = Customer()
        test_customer.overrite_name("test")
        self.assertEqual(test_customer.get_name(), "test")
    
    # UNIT TESTS FOR INGREDIENT CLASS
    def test_get_name(self):
        test_ingredient = Ingredient("cashew milk tea", "base")
        self.assertEqual(test_ingredient.get_name(), "cashew milk tea")
    
    def test_get_type(self):
        test_ingredient = Ingredient("cashew milk tea", "base")
        self.assertEqual(test_ingredient.get_type(), "base")

    # UNIT TESTS FOR INVENTORY CLASS    
    def test_get_length(self):
        test_inventory = Inventory()
        test_inventory.add_item(Ingredient("cashew milk tea", "base"))
        test_inventory.add_item(Ingredient("boba", "boba"))
        test_inventory.add_item(Ingredient("strawberry", "topping"))
        self.assertEqual(test_inventory.get_length("base"), 1)
        self.assertEqual(test_inventory.get_length("boba"), 1)
        self.assertEqual(test_inventory.get_length("topping"), 1)
    
    # INTEGRATION TESTS FOR ORDER AND INGREDIENT CLASS
    def test_get_base(self):
        test_order = Order(Ingredient("cashew milk tea", "base"), Ingredient("plain boba", "boba"), Ingredient("strawberry", "topping"))
        self.assertEqual(test_order.get_base(), "cashew milk tea")
    
    def test_get_boba(self):
        test_order = Order(Ingredient("cashew milk tea", "base"), Ingredient("plain boba", "boba"), Ingredient("strawberry", "topping"))
        self.assertEqual(test_order.get_boba(), "plain boba")

    def test_get_toppings_empty(self):
        test_order = Order(Ingredient("cashew milk tea", "base"), Ingredient("plain boba", "boba"), '')
        self.assertEqual(test_order.get_toppings(), "no toppings")
    
    def test_get_toppings_full(self):
        test_order = Order(Ingredient("cashew milk tea", "base"), Ingredient("plain boba", "boba"), Ingredient("strawberry", "topping"))
        self.assertEqual(test_order.get_toppings(), "strawberry")
    
    # INTEGRATION TESTS FOR INVENTORY AND INGREDIENT CLASS
    def test_remove_item_invalid(self):
        test_inventory = Inventory()
        self.assertEqual(test_inventory.remove_item(Ingredient("cashew milk tea", "base")), False)
    
    def test_get_item_by_name(self):
        test_inventory = Inventory()
        test_inventory.add_item(Ingredient("cashew milk tea", "base"))
        test_inventory.add_item(Ingredient("boba", "boba"))
        test_inventory.add_item(Ingredient("strawberry", "topping"))
        self.assertEqual(test_inventory.get_item_by_name("cashew milk tea").get_name(), "cashew milk tea")
    
    def test_get_item_by_name_invalid(self):
        test_inventory = Inventory()
        test_inventory.add_item(Ingredient("cashew milk tea", "base"))
        test_inventory.add_item(Ingredient("boba", "boba"))
        test_inventory.add_item(Ingredient("strawberry", "topping"))
        self.assertEqual(test_inventory.get_item_by_name("test"), None)

    def test_get_bases(self):
        test_inventory = Inventory()
        test_base = Ingredient("cashew milk tea", "base")
        test_inventory.add_item(test_base)
        self.assertEqual(test_inventory.get_bases()[0].get_name(), test_base.get_name())
    
    def test_get_bobas(self):
        test_inventory = Inventory()
        test_boba = Ingredient("boba", "boba")
        test_inventory.add_item(test_boba)
        self.assertEqual(test_inventory.get_bobas()[0].get_name(), test_boba.get_name())
    
    def test_get_toppings(self):
        test_inventory = Inventory()
        test_topping = Ingredient("strawberry", "topping")
        test_inventory.add_item(test_topping)
        self.assertEqual(test_inventory.get_toppings()[0].get_name(), test_topping.get_name())

if __name__ == '__main__':
    unittest.main()