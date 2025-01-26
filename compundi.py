principle =0
rate=0
time=0
while principle<=0:
    principle=float(input("What is the principle "))
    if principle<=0:
        print("Principle can't be less then or equal to zero")

while rate<=0:
    rate=float(input("What is the rate "))
    if rate<=0:
        print("rate can't be less then or equal to zero")

while time<=0:
    time=float(input("What is the time "))
    if time<=0:
        print("time can't be less then or equal to zero")

total= principle*pow((1+rate/100), time)
print(f"Balance after {time} year/s: ${total :.2f}")