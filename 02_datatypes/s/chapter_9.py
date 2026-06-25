essential_spices={"cardamom","ginger","cinnaon"}
optional_spices={"cloves","ginger","black pepper"}
all_spices=essential_spices|optional_spices
print(f"All spices needed: {all_spices}")
common_spices=essential_spices&optional_spices
print(f"Common spices: {common_spices}")
only_in_essential=essential_spices-optional_spices
print(f"Spices only in essential: {only_in_essential}")
print(f"Is 'cloves' an optional spice? {'cloves' in optional_spices}")