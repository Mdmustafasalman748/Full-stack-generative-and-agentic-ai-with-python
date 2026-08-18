class chai():
    def __init__(self,sweetness,milk_level):
        self.sweetness=sweetness
        self.milk_level=milk_level
    def sip(self):
        print(f"Sipping chai")
    def add_sugar(self,amount):
        print(f"Added the sugar")
    
my_chai=chai(sweetness="3", milk_level="2")
my_chai.add_sugar(3)