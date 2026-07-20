def chai_flavor(flavor="masala"):
    """Return the flavor of chai"""
    return flavor
print(chai_flavor.__doc__)
print(chai_flavor.__name__)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param chai: Number of chai cups (10 dollars each)
    :param samosa: Number of samosa (5 dollars each)
    :return: (total amount, thank you message as string)
    """
    total = chai * 10 + samosa * 5
    return total, "Thank you for visiting chaicode.com"
print(generate_bill.__doc__)
print(generate_bill.__name__)