class Order():
    def __init__(self, base, boba, toppings):
        self.base = base
        self.boba = boba
        self.toppings = toppings
    
    def get_base(self):
        return self.base.get_name()
    
    def get_boba(self):
        return self.boba.get_name()

    def get_toppings(self):
        if self.toppings == '':
            return "no toppings"
        return self.toppings.get_name()
        