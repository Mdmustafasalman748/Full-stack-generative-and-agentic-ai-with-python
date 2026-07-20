chai="Ginger chai"
def prepare_chai(order):
    print("Preparing", order)
    
prepare_chai(chai)
print(chai)

chai=[1,2,3]
def edit_chai(cup):
    cup[1]=42
    
edit_chai(chai)
print(chai)

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)
    
make_chai("black","yes","low") #positional
make_chai(tea="green",sugar="medium",milk="no") #keyword

def special_chai(*ingredients, **extra):
    print("Ingredients:",ingredients)
    print("Extra:",extra)
special_chai("Cinnamon","Cardamom",sweetner="Honey",foam="yes")

def chai_order(order=[]):
    order.append("masala")
    print(order)
    
chai_order()
chai_order()

def chai_order(order=None):
    if order is None:
        order=[]
    print(order)
    
chai_order()
chai_order()