#1.
import recipes.flavors
print(recipes.flavors.ginger_chai())

#2.
from recipes.flavors import elachai_chai,ginger_chai
print(ginger_chai())

#3.
from .recipes.flavors import ginger_chai
print(ginger_chai())