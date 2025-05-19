import random

#MAKE GUESS NUMBER
#IF NUMBER IS RIGHT, PRINT THAT , IF WRONG, PRINT IS WRONG

def numbergame():
    number = random.randint(
        1, 10
    )
    selected_number = number

    guess = input("Please pick a number between 1 and 10! ")

    if selected_number == guess:
        print(f'Correct! The number was {selected_number}!')
    else:
        print(f"Wrong choice! The number was {selected_number}")


numbergame()