is_boiling=True
stri_count=5
total_actions=stri_count+is_boiling #upcasting
print(f"Total actions: {total_actions}")
milk_present=0
print(f"Is milk present? {bool(milk_present)}")
water_hot=True
tea_added=False
can_serve=water_hot and tea_added
print(f"Can we serve the tea? {can_serve}")
