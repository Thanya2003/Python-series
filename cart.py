menu={
    "pizza": 3.5,
    "fires":5,
    "nachos":6.25,
    "burger":4.25,
    "chips":3.25,
    "soda":5.25,
    "lemonade":6
}
cart=[]
total=0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10} : ${value: .2f}")
print("---------------------------")

while True:
    food = input("Select the Food Item (q to quit)").lower()
    if food== "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------------------")
for foods in cart:
    total+=menu.get(foods)
    print(foods, end=" ")

print()
print(f"Total: ${total: .2f}")
