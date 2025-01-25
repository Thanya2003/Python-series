operator=input("Enter the operator (+ * - /) ")
num1=float(input("Enter the number1 "))
num2=float(input("Enter the number2 "))

if operator=="+" :
    result=num1+num2
    print(f"{num1} {operator} {num2} => {result}")

elif operator == "-":
    result =num1-num2
    print(f"{num1} {operator} {num2} => {result}")

elif operator == "*":
    result=num1*num2
    print(f"{num1} {operator} {num2} => {result}")

elif operator == "/":
    if num2 == 0:
        print("Num2 should be greater than zero")
    else:
        result=num1/num2
        print(f"{num1} {operator} {num2} => {result}")
else:
    print("Invalid operation")
