capital={"USA":"Washington D C", "India":"New Delhi", "Japan":"Tokyo", "Germany":"Berlin"}

# print(capital.get("USA"))
# capital.update({"India":"Bengaluru"})
# capital.pop("USA")
# capital.popitem()
# capital.clear()
# print(capital)

# key=capital.values()
# key=capital.keys()
# for keys in key:
#     print(keys)

# print(key)

# for value in key:
#     print(value)


item=capital.items()
for key, value in capital.items():
    print(f"{key} : {value}")
