class Inventory():
    def __init__(self):
        self.stock = []
    
    def add_item(self, item):
        self.stock.append(item)

    def remove_item(self, item):
        # ensure item exists
        if item not in self.stock:
            return False
        else:
            self.stock.remove(item)
    
    def set_stock(self, stock):
        self.stock = stock

    def get_stock(self):
        return self.stock
    
    def get_length(self, type):
        count = 0
        for item in self.stock:
            if item.get_type() == type:
                count += 1
        return count
    
    def get_bases(self):
        bases = []
        for item in self.stock:
            if item.get_type() == "base":
                bases.append(item)
        return bases
    
    def get_bobas(self):
        bobas = []
        for item in self.stock:
            if item.get_type() == "boba":
                bobas.append(item)
        return bobas
    
    def get_toppings(self):
        toppings = []
        for item in self.stock:
            if item.get_type() == "topping":
                toppings.append(item)
        return toppings
    
    def get_item_by_name(self, name):
        for item in self.stock:
            if item.get_name() == name:
                return item
        return None