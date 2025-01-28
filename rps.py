import random

options=("rock", "paper", "scissors")
running=True

while running:
    player = None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter a choice (rock, paper, scissors): ")
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player not in options:
            print("enter the valid rock paper scissors")
        elif player=="rock" and computer=="scissors":
            print("You Win!!..")
        elif player=="paper" and computer=="rock":
            print("You Win!!..")
        elif player==computer:
            print("It's Tie!!..")
        elif player=="scissors" and computer=="paper":
            print("You win!!..")
        else:
            print("You Lose!!..")
        
        
        if not input("Play Again? (y/n): ").lower() =="y":
            running= False
print("Thanks for Playing!")
