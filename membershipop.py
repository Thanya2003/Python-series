# string
word="Apple"

letter=input("Guess the letter in the word ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"The letter is not found in the {word}")


# list
students=["Thanya", "Dhanya", "Aadhya", "Dhritya"]

student= input("Enter the Student name ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not found")

#dectionary
grades={"Thanya": "A", "Dhanya": "B", "Aadhya": "C", "Dhritya":"D"}
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not found")


