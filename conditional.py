x=50
num=6
age=20
weather =10
user = "guest"

# print("Positive " if x>=0 else "Negative")
res="EVEN" if num%2==0 else "ODD"
status = "Adult" if age >=18 else "Child"
temp ="HOT" if weather>20 else "COLD"
access_level= "Full Access" if user == "Admin" else "Limited Access"


print(access_level)