#Tuples
masala_spices=("Cardamom", "Cloves", "Cinnamon")
(spice1, spice2, spice3)=masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
ginger_ratio, cardamom_ratio=2,1
print(f"ginger ratio: {ginger_ratio}, cardamom ratio: {cardamom_ratio}")
ginger_ratio,cardamom_ratio=cardamom_ratio, ginger_ratio
print(f"After swapping: ginger ratio: {ginger_ratio}, cardamom ratio: {cardamom_ratio}")

#Membership
print(f"Is 'Cinnamon' in masala spices? {'Cinnamon' in masala_spices}")
