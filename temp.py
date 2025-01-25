unit = input("Is this temperature in celsius or Fahrenhit (F/C) ")
temp=float(input("what is temperature "))

if unit == "C":
    temp=round((temp*9)/5+32,1)
    print(f"The temperature is fahernhit {temp}F")
elif unit == "F":
    temp=round((temp-32)*5/9,1)
    print(f"The temperature is celsius {temp}C")
else:
    print("Invalid Tempature Unit")