def chai_customer():
    print("Welcome! What chai would you like?")
    order=yield
    while True:
        print(f"Preparing your {order}...")
        order=yield
stall=chai_customer()
next(stall)
stall.send("Masala chai")
stall.send("Lemon chai")