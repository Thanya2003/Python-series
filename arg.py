def add(*arg):
    temp=0
    for args in arg:
        temp+=args
    return temp

print(add(10, 11, 12))

def name(*name):
    for names in name:
        print(names, end=" ")

name("Thanya", "shettigar")