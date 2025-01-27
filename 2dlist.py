fruits=["Apple", "Orange", "Pineapple", "Mango"]
vegetables=["Potato", "Tomato", "Carrot"]
meat=["Fish", "Chicken", "Mutton"]

gorcery=[fruits, vegetables, meat]

for collection in gorcery:
    for food in collection:
        print(food, end=" ")
    print()