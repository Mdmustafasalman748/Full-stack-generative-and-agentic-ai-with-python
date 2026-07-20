chai_menu={"masala":30,"ginger":40}
chai_menu=["elaichi"] #key error
#To fix error
try:
    chai_menu=["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")
print("Hello chai code")