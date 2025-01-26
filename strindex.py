# indexing = [start : end : step]

credit_number = "1234-5678-9101-1235"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])

# last_digits of the credit card number
Last=credit_number[::-1]
# print(f"XXXX-XXXX-XXXX-{Last}")
# print(Last)

email = input("Enter Your email Id ")
index = email.index("@")
username = email[:email.index("@")]
domain=email[email.index("@")+1:]

print(f"Your Username is {username} and domain is {domain}")