import random
def spin_row():
    symbols=["🍏", "🍊", "🍒", "🍉", "🍌", "💫"]
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("************")
    print(" | ".join(row))
    print("************")

def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍏":
            return bet*5
        elif row[0]=="🍊":
            return bet*10
        elif row[0]=="🍒":
            return bet*15
        elif row[0]=="🍉":
            return bet*20
        elif row[0]=="🍌":
            return bet*25
        elif row[0]=="💫":
            return bet*100
    else:
        return 0
def main():
    balance=100

    print("***********************")
    print("Welcome to Python Slot")
    print("Symbols : 🍏 🍊 🍒 🍉 🍌")
    print("***********************")

    while balance>0:
        print(f"Current Balance: {balance}")

        bet = input("Place your bet amount ")
        if not bet.isdigit():
            print("Please enter valid number")
            continue
        bet=int(bet)
        if bet > balance:
            print("Insuffient balance")
            continue
        if bet <=0:
            print("Bet must be greater than Zero")
            continue
        balance-=bet
        row=spin_row()
        print("Spining......")
        print_row(row)
        payout= get_payout(row, bet)
        if payout > 0:
            print(f"You won ₹{payout}")
        else:
            print("Sorry you lost in this round paly again")
        
        balance+=payout

        play_again=input("If you want to spin again(Y/N) ")
        if play_again != 'Y':
            break
    print("*******************************************")
    print(f"Game Over your final Balance is ₹{balance}")
    print("*******************************************")


if __name__ =='__main__':
    main()
