# def bill(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount: .2f} is due : {due_date} ")

# bill("Thanya",402, "01/02/2024")

# def add(x, y):
#     z=x+y
#     return z

# def subtract(x, y):
#     z=x-y
#     return z

# def mul(x, y):
#     z=x*y
#     return z

# def div(x, y):
#     z=x/y
#     return z

# print(add(4, 5))
# print(subtract(4, 5))
# print(mul(4, 5))
# print(div(4, 5))

# posistional argument
def create_name(first, last):
    first= first.capitalize()
    last= last.capitalize()
    return first+" "+last

print(create_name("thanya", "shettigar"))