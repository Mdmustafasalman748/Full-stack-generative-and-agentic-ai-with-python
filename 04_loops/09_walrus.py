# value=13
# remainder=value%5
# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value=13
if remainder:=value%5:
    print(f"Not divisible, remainder is {remainder}")
    
available_size=["small","medium","large"]
if(requested_size:=input("Enter your chaicup size:")) in available_size:
    print(f"Serving {requested_size} chai cup")
else:
    print(f"Size is unavailable {requested_size} ")
    
flavors=["masala","ginger","lemon","mint"]
print(f"Available flavours: {flavors}")
while(flavors:=input("Enter your favorite flavor:")) not in flavors:
    print(f"Sorry!Flavor {flavors} is not available")
print(f"You choose {flavors} chai")