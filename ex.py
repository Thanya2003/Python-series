foods=[]
prices=[]
total=0

while True:
    food=input("What is a food that you want to buy (q to quit) : ")
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the {food} for the price: $  "))
        foods.append(food)
        prices.append(price)
print("-----------Your cart-----------")    
for food in foods:
    print(food)

for price in prices:
    total+=price

print(f"Your Total is: ${total}")