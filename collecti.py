# list =[] ordered and chnageable. duplicates ok
# set = {} unordered and immutable.  No duplictes 
#  tuple= () ordered and unchangeable. duplicates ok

fruits =["Apple", "Orange", "Banana", "Coconut"]

print(dir(fruits))

help(list)

fruits[1]="pineapple"

print(len(fruits))

fruits.append("Pineapple")
fruits.remove("Apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.count("Banana"))
print(fruits.index("Apple"))


print(fruits[:3])
for fruit in fruits:
    print(fruit)