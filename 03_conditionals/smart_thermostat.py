device_status="active"
temperature=int(input("Enter temperature:"))
if device_status=="active":
    if temperature>35:
        print("Hight temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")