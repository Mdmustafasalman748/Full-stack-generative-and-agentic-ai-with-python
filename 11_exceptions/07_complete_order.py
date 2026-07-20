class InvalidOrderError(Exception):
    pass
def bill(flavor,cups):
    menu={"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise InvalidOrderError("Flavor not available")
        if not isinstance(cups,int):
            raise TypeError("Cups must be an integer")
        total=menu[flavor]*cups
        print(f"Your total bills for {cups} of {flavor} chai: ${total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for your order!")
        
bill("mint",2)
bill("masala","three")
bill("ginger",3)