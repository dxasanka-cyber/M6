import math
def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius /100) **2
    return price/area
d1 = float(input("Give the diameter of the first pizza :"))
p1 = float(input("Give the price of the first pizza :"))

d2 = float(input("Give the diameter of the second pizza :"))
p2 = float(input("Give the price of the second pizza :"))
pizza1 = unit_price(d1, p1)
pizza2 = unit_price(d2, p2)
print ("Unite price of first pizza is", pizza1)
print ("Unite price of second pizza is", pizza2)

if pizza1 < pizza2:
    print("First pizza has better unite price")
elif pizza2 < pizza1:
    print("Second pizza has better unite price")
else:
    print("The unit price was the same.")
