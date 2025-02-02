from wordlist import words
import random



hangman_art={
    0:("        ",
       "        ",
       "        "),
    1:("    o    ",
       "        ",
       "        "),
    2:("    o    ",
       "    |    ",
       "        "),
    3:("    o    ",
       "  / |    ",
       "        "),
    4:("    o    ",
       "  / | \\ ",
       "        "),
    5:("    o    ",
       "  / | \\ ",
       "   /   "), 
    6:("    o    ",
       "  / | \\ ",
       "   / \\  "),        
}
def display_man(worng_ans):
    for line in hangman_art[worng_ans]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))
def display_anst(answer):
    print(" ".join(answer))


def main():
    answer=random.choice(words).lower()
    hint=["_"]*len(answer)
    wrong_ans=0
    guessed_letter=set()
    is_running=True
    while is_running:
        display_man(wrong_ans)
        display_hint(hint)
        guess=input("Enter a letter ").lower()

        if len(guess)!=1 or not guess.isalpha():
            print("Invalid Guess")
            continue
        if guess in guessed_letter:
            print("Letter is already guessed")
            continue

        guessed_letter.add(guess)    

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_ans+=1
        
        if "_" not in hint:
            display_man(wrong_ans)
            display_anst(answer)
            print("YOU WIN!...")
            is_running=False
        elif wrong_ans>=len(hangman_art)-1:
            display_man(wrong_ans)
            display_anst(answer)
            print("YOU Lose!...")
            is_running=False

if __name__=="__main__":
    main()