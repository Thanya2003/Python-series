weight = int(input("What is the weight:"))
unit = input("Kilogram and Pound (K or L)")

if unit == "K":
    weight=weight*2.206
    print(f"Your weight {weight} Lbs")
elif unit == "L":
    weight=weight/2.206
    print(f"Your weight {weight} kgs")
else:
    print("Invalid Units")