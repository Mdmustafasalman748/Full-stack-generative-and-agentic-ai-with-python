file=open("order.txt","w")
try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()
#or 

with open("orders.txt","w") as file:
    file.write("Ginger tea - 4 cups")