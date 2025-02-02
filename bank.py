def show_balance(balance):
    print("**************************")
    print(f"Your Balance is ₹{balance : .2f}")
    print("**************************")


def deposit():
    print("**************************")
    amount=float(input("Enter the amount to be deposit "))
    print("**************************")

    if amount < 0:
        print("**************************")
        print("It is a invalid amount")
        print("**************************")
        return 0
    else:
        return amount

def withdrawal(balance):
    print("**************************")
    amount=float(input("Enter the amount to be withDrawal "))
    print("**************************")
    if amount > balance:
        print("**************************")
        print("Insufficient balance")
        print("**************************")
        return 0
    elif amount<0:
        print("**************************")
        print("That's invalid amount")
        print("**************************")
        return 0
    else:
        return amount
    
def main():
    balance=0
    is_running=True

    while is_running:
        print("**************************")
        print("      Banking Program     ")
        print("**************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. WithDrawn")
        print("4. Exit")
        print("**************************")
        choice=int(input("Enter your choice 1-4 "))
        print("**************************")


        if choice==1:
            show_balance(balance)
        elif choice==2:
            balance+=deposit()
        elif choice == 3:
            balance-=withdrawal(balance)
        elif choice==4:
            is_running=False
        else:
            print("**************************")
            print("This is an invalid choice")
            print("**************************")

    print("**************************")
    print("Thank You Have nice day")
    print("**************************")

if __name__=='__main__':
    main()