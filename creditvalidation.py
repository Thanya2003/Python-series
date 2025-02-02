card_odd_didgit=0
card_even_didgit=0
total=0

card_number=input("Enter the Credit card number ")
card_number=card_number.replace("-","")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]

for x in card_number[::2]:
    card_odd_didgit+=int(x)

for x in card_number[1::2]:
    x = int(x)*2
    if x>=10:
        card_even_didgit+=(1+(x%10))
    else:
        card_even_didgit+=x

total=card_even_didgit+card_odd_didgit

if total%10 ==0:
    print("Valid")
else:
    print("Inavlid")
