flavours=["ginger","out of stock","lemon","discontinued","tulsi"]
for flavour in flavours:
    if flavour=="out of stock":
        continue
    if flavour=="discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")
print(f"Outside of loop")