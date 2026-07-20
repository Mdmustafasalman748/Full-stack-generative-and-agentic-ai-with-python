def my_decorators(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper
@my_decorators
def greet():
    print("Hello from decorators class from chaicode")
greet()
print(greet.__name__) 

#To preserve the function name use wraps
from functools import wraps

def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper
@my_decorators
def greet():
    print("Hello from decorators class from chaicode")
greet()
print(greet.__name__)