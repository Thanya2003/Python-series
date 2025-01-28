# positional argument follows keyword argument
def full_name(first, last, greeting, title):
    print(f"{greeting} {title} {first} {last}")

full_name("Thanya", last="shettigar", title="Ms.", greeting="Hellow")