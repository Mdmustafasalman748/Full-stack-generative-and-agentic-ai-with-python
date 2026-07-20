class chaiorder:
    def __init__(self, type_, size):
        self.type=type_
        self.size=size
    def summary(self):
        return f"A {self.size} ml cup of {self.type} chai"

order=chaiorder("Masala", 200)
print(order.summary())

order_two=chaiorder("Ginger", 220)
print(order_two.summary())