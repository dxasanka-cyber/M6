def convert(g):
    return g * 3.785
gallons = float(input("Enter gallons: "))
while gallons >= 0:
    liters = convert(gallons)
    print("Liters:", liters)
    gallons = float(input("Enter gallons: "))
    print("Program ends")

