chai_order=dict(type="Masala_chai",size="Large",sugar=2)
print(f"Chai order details: {chai_order}")
chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")
print(f"Is sugar in order? {'sugar' in chai_order}")
chai_order={"type":"Ginger_chai","size":"Medium","sugar":1}
print(f"Order details(keys): {chai_order.keys()}")
print(f"Order details(values): {chai_order.values()}")
print(f"Order details(items): {chai_order.items()}")
last_item=chai_order.popitem()
print(f"Last item removed: {last_item}")
extra_spices={"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Updated recipe: {chai_recipe}")
chai_size=chai_order["size"]
print(f"Chai size: {chai_size}")
customer_note=chai_order.get("customer_note","NO NOTE")
print(f"Customer note: {customer_note}")