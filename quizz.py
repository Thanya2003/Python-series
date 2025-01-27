questions=("How many elements are in the periodic table?:",
           "Which animal lays the largest eggs?:",
           "What is the most abundant gas in earth atmospere?:",
           "How many bones are in the human body?:",
           "Which is the hottest planet in the solar system?:")

option=(("A.116", "B.117", "C.118", "D.119"),
        ("A.WHALE", "B.Crocodile", "C.Elephant", "D.Ostrich"),
        ("A.Nitrogen", "B.Oxygen", "C.Carbon-dioxide", "D.Hydrogen"),
        ("A.206", "B.207", "C.208", "D.209"),
        ("A.Mercury", "B.Venus", "C.Earth", "D.Mars"))

answers=("C","D","A","A","B")
GUESS=[]
que_number=0
score=0
print(option[0])
for que in questions:
    print("-------------------------------")
    print(que)
    for optio in option[que_number]:
        print(optio)
    quesses=input("Enter A/B/C/D ").upper()
    GUESS.append(quesses)
    if quesses==answers[que_number]:
        print(" Correct!!...")
        score+=1
    else:
        print("Incorrect!!...")
        print(f"{answers[que_number]} is the Correct Answer!!...")

    que_number+=1
print("------------------------")
print("Answers:", end=" ")
for ans in answers:
    print(ans, end=" ")
print()
print("Guess:", end=" ")
for gues in GUESS:
    print(gues, end=" ")
print()
print("------------------------")
print()
print("------------------------")
score=int(score/len(questions)*100)
print(f"TOtal score is {score}%")
print("-----------------------")