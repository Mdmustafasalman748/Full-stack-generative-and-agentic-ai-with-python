favourite_chais=["Masala Chai", "Green Tea", "Masala Chai",
                 "Lemon Tea","Green Tea", "Elaichi Chai"]

unique_chai={chai for chai in favourite_chais}
print(unique_chai)

recipes={
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai":["cardamon","milk"],
    "Spicy Chai":["ginger","black pepper", "clove"]
}

unique_spices={spice for ingrediants in recipes.values() for spice in ingrediants}
print(unique_spices)