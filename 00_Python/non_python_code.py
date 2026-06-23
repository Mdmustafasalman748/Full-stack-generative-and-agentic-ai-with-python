def make_chai:
    if not kettle_has_water:
        fill_kettle()
        plug_in_kettle()
        boil_water()
    if not is_cup_clean:
        wash_cup()
    add_to_cup("Tea leaves")
    add_to_cup("Sugar")
    pour("Boiled water")
    stir("cup")
    serve("chai")
    