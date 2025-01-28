# def net_price(price, discount=0, tax=0.05):
#     return price *(1-discount)*(tax + 1)

# print(net_price(500))

import time
# default agrument = non default argument must follow default argument
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)

    print("DONE!!...")

count(30, 25)