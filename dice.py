# ● ┌ ─ ┐ │ └ ┘
import random
dice=[]
total=0


dice_art={
    1:( "┌───────────┐",
        "│           │",
        "│           │",
        "│     ●     │",
        "│           │",
        "│           │",
        "└───────────┘"),
    2:( "┌───────────┐",
        "│           │",
        "│  ●        │",
        "│           │",
        "│         ● │",
        "│           │",
        "└───────────┘"),
    3:( "┌───────────┐",
        "│  ●        │",
        "│           │",
        "│     ●     │",
        "│           │",
        "│         ● │",
        "└───────────┘"),
    4:( "┌───────────┐",
        "│           │",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "│           │",
        "└───────────┘"),
    5:( "┌───────────┐",
        "│           │",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "│           │",
        "└───────────┘"),
    6:( "┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘")
}

number_of_dice=int(input("How many Dice?: "))
for die in range(number_of_dice):
    dice.append(random.randint(1, 6))

    # for die in range(number_of_dice):
    #     for line in dice_art.get(dice[die]):
    #         print(line)

for line in range(7):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for die in dice:
    total+=die
print(f"Total: {total}")
