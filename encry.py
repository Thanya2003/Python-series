import random
import string

chars =" "+ string.digits + string.punctuation + string.ascii_letters
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)

# print(f"chars : {chars}")
# print(f"Keys : {keys}")


#encryption
message = input("Enter the message to be encryption: ")
cipher_txt=""

for letter in message:
    index = chars.index(letter)
    cipher_txt+=keys[index]

print(f"Orginal Message: {message}")
print(f"Encrypted Message: {cipher_txt}")

#decryption
cipher_txt = input("Enter the message to be decryption: ")
message=""

for letter in cipher_txt:
    index = keys.index(letter)
    message+=chars[index]


print(f"Encrypted Message: {cipher_txt}")
print(f"Orginal Message: {message}")