# def make_chai():
#     if not kettle_has_water():
#         fill_kettle()
#     plug in kettle()
#     boil_water()
#     if not is_cup_clean():
#         was_Cup()
#     add_to_cup("Tea leaves")
#     add_to_cup("Sugar")
#     pour("Boiled water")
#     stir("cup")
#     serve("chai")
    
class chai:
        def __init__(self, sweetness,milk_level):
            self.sweetness = sweetness
            self.milk_level = milk_level
        def sip(self):
            print("sipping the chai")
        def add_sugar(self, amount):
            print("added the sugar")
            
my_chai=chai(sweetness="3", milk_level="2")
my_chai.add_sugar(3)
my_chai.sip()

import sys
print(sys.version)