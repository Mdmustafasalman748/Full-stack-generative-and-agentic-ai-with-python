masala_spices=('Cardamom', 'Cloves', 'Cinnamon')
(Spice1, Spice2, Spice3)=masala_spices
print(f"Main masala spices: {Spice1}, {Spice2}, {Spice3}")
ginger_ratio, cardamom_ratio=2,1
print(f"ginger ratio: {ginger_ratio}, cardamom ratio: {cardamom_ratio}")
ginger_ratio,cardamom_ratio=cardamom_ratio, ginger_ratio
print(f"After swapping: ginger ratio: {ginger_ratio}, cardamom ratio: {cardamom_ratio}")
#Membership
print(f"Is 'Cinnamon' in masala spices? {'Cinnamon' in masala_spices}")