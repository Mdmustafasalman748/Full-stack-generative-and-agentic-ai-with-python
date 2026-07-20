class OutOfIngredientsError(Exception):
    pass
def make_chai(milk,sugar):
    if milk==0 or sugar==0:
        raise OutOfIngredientsError("Not enough ingredients to make chai")
    print("Chai is ready to serve!")
make_chai(0,1)