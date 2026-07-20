import recipes.flavors
print(recipes.flavors.ginger_chai())

from recipes.flavors import elachai_chai,ginger_chai
print(elachai_chai())
print(ginger_chai())

#from .recipes.flavors import ginger_chai