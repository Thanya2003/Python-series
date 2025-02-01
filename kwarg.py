def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    
address(stree="&th cross", landmark="Srigandha nagar", place="Heggnalli", city="Bengaluru", District="Udupi")


def shipping_label(*args, **kwargs):
    for name in args:
        print(name, end=" ")
    print()
    
    print(f"{kwargs.get('stree')}")
    print(f"{kwargs.get('landmark')} {kwargs.get('place')}")



shipping_label("Ms", "Thanya", "Shettigar", stree="&th cross", landmark="Srigandha nagar", place="Heggnalli", city="Bengaluru", District="Udupi")