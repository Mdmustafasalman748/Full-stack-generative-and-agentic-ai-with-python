def make_chai():
    return "Here is your masala chai" 
print(make_chai())

def make_chai():    
    return "Here is your masala chai"   
    print("Here is your masala chai")
return_value=make_chai()
print(return_value)

def idle_chaiwala():
    pass
print(idle_chaiwala())

def sold_cups():
    return 120
total=sold_cups()
print(total)

def chai_Status(cups_left):
    if cups_left==0:
        return "Sorry! chai over"
    return "Chai is ready"
    print("chai")
print(chai_Status(0))
print(chai_Status(5))

def chai_report():
    return 100,20,10 #sold, remaining

sold,remaining,not_paid=chai_report()
print(f"Sold chai cups: {sold}")
print(f"Remaining chai cups: {remaining}")
print("Not paid:",not_paid)