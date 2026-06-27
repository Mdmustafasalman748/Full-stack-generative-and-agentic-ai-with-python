def serve_chai():
    chai_type="Masala" #local scope
    print(f"Inside function {chai_type}")

chai_type="Lemon"
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order="lemon" #enclosing scope
    def print_order():
        chai_order="ginger" #local scope
        print("Inner:",chai_order)
    print_order()
    print("Outer:",chai_order)
    
chai_order="Tulsi" #global scope
chai_counter()
print("Global:",chai_order)
    