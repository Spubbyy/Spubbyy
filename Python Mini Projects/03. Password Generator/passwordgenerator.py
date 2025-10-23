### PASSWORD GENERATOR
import random
import string
import time
import secrets

length = 12 # password character length, change the number to set the character amount
passwordcharacters = string.ascii_letters + string.digits #### uses the string library to select all the characters and stuff


user = input("Please enter your username: ")
print(f'Hello {user}! Please wait as we generator you a new password of {length} characters!')


include_symbols = input("Would you like to include symbols? Y/N ").lower
if include_symbols == "Y" or "yes":
    passwordcharacters += string.punctuation

password = ''.join(secrets.choice(passwordcharacters) for _ in range(length)) 

time.sleep(2)

print(f'Your new password is: {password}')

with open("vault.txt", "a") as file:
    file.write(password + "\n")

print("Password saved to vault.txt")
