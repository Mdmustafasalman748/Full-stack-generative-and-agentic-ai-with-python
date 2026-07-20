orders=["masala","ginger"]
#print(orders[2]) #IndexError

try:
    print(orders[2])
except IndexError:
    print("Index out of range")