class Ship:
    base_charge = 4000
    def __init__(self, basefare, tax_amount):
        self.basefare = basefare
        self.tax_amount = tax_amount

    def update_charges(self):
        self.basefare += 2000
        self.tax_amount -= 2000

    def update_tax(self):
        custom_tax = 3000
        self.tax_amount += custom_tax

class Cruise(Ship):
    def __init__(self, basefare, tax_amount, ballroom_fee):
        super().__init__(basefare, tax_amount)
        self.ballroom_fee = ballroom_fee
    
    def update_charges(self):
        self.tax_amount *= 3 
        self.tax_amount += Ship.base_charge
        super().update_tax()
        print(self.tax_amount)

    def update_fare(self):
        super().update_charges()
        self.basefare += self.ballroom_fee
        print(self.basefare)
        print(self.tax_amount)

cruise_obj = Cruise(5000, 200, 3000)
cruise_obj.update_charges()
cruise_obj.update_fare()