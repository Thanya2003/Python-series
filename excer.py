user_input=input("enter the user name ")
if len(user_input)>12 :
    print("Your username can't be more then 12 character")
elif user_input.find(" ")>0:
    print("username should not have space between them")
elif not user_input.isalpha():
    print("Your userName can't contain numbericals or special characters")
else:
    print(f"welcome {user_input}")
