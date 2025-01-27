import random
low=1
high=100
number=random.randint(low, high)

guesses=0

while True:
    guess=int(input(f"Guess the number between ({low}-{high})"))
    guesses+=1
    if guess>number:
        print(f"{guess} is too high")
    elif guess<number:
        print(f"{guess} is too low") 
    else:
        print(f"{guess} is correct !!..")
        break
print(f"This took rounds of {guesses}")