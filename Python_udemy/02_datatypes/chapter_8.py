ingredients=["water","milk","black tea"]
print(f"Ingredients are: {ingredients}")
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")
spice_options=["ginger","cardamom"]
chai_ingredients=["water","milk"]
chai_ingredients.extend(spice_options)
print(f"Chai ingredients: {chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"Chai ingredients after inserting black tea: {chai_ingredients}")
last_added=chai_ingredients.pop()
print(f"Last added ingredient: {last_added}")
print(f"Chai ingredients after popping last added: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Chai ingredients in reverse order: {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai ingredients sorted: {chai_ingredients}")
sugar_levels=[1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")