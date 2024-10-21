# def SayHello(name):
#     print("Hello {}! How are you?".format(name))
#     return
# import Hello
# hello.sayhello("abc")
# #print(hello._name_)

# import math
# dir(math)

"""Develop a game for lucky number
we will provide 3 changes to user to enter his/her lucky number
if matches with system generated number user will declared as won or otherwise lost
score will be first attempt match score =10
score will be second attempt match score =7
score will be third attempt match score =5
"""
import random

def lucky_number_game():

    system_lucky_number = random.randint(1, 100)

    score_attempts = {1: 10, 2: 7, 3: 5}
    
    print("Welcome to the Lucky Number Game!")
    print("You have 3 chances to guess your lucky number (between 1 and 100).")


    for attempt in range(1, 4):
        try:
            user_guess = int(input(f"Attempt {attempt}: Enter your lucky number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_guess == system_lucky_number:
            print(f"Congratulations! You've guessed the lucky number in attempt {attempt}.")
            print(f"You've won with a score of {score_attempts[attempt]}!")
            break
        else:
            print(f"Sorry, that's not the lucky number. You have {3 - attempt} attempts left.")
    else:
        print(f"Game Over! The lucky number was {system_lucky_number}. Better luck next time!")


lucky_number_game()