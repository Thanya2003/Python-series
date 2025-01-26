row=int(input("Enter the number of rows "))
column=int(input("Enter the number of column "))
symbol=input("Enter the symbol ")

for x in range(row):
    for y in range(column):
        print(symbol,end="")
    print()
