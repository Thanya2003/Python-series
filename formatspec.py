# format specifer {value: flag}
price = 3.14458
price1= -96.25
price3= -7890000.145

# print(f"price 1 is {price : .2f}")
# print(f"price 2 is {price1: .2f}")
# print(f"price 3 is {price3: .2f}")

# print(f"price 2 is {price1: >10}") #right align
# print(f"price 1 is {price : 10}")
# print(f"price 3 is {price3: <10}") #left align
# print(f"price 3 is {price3: ^10}") #justify align

print(f"price 1 is {price :+}")
print(f"price 2 is {price1:+}")
print(f"price 3 is {price3:,}")


print(f"price 3 is {price3:+,.2f}")
