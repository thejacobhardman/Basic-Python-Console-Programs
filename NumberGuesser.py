################################################################################
#                     Lab 1 – A Python Program                                 #
#                                                                              #
# PROGRAMMER:        [your name] [your email address]                          #
# CLASS:             [CS160 or CS200]                                          #
# TERM:              Spring 2021                                               #
# INSTRUCTOR:                                                       #
# SUBMISSION DATE:   [date of submission]                                      #
#                                                                              #
# DESCRIPTION                                                                  #
# [Include a brief but complete description of the problem the code is         #
# solving.]                                                                    # 
#                                                                              #
# ORIGINAL SOURCE                                                              #
# This code was originally written by:                                         #
#    Author:   [writer of original program]                                    #
#    Location: [indicate location, such as a website or textbook]              #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is copyright (c)2021 [original-author-name], [your-name] and    #
#                                                                #
#                                                                              #
################################################################################

import random, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Generate_Random_Num():
    return random.randint(1, 10)

is_running = True
while is_running:
    cls()

    num = Generate_Random_Num()

    print("I'm thinking of a number between 1 and 10! Can you guess it?")

    is_num_guessed = False
    while not is_num_guessed:
        guess = int(input("Guess a number: "))

        if guess < num:
            print(f"Wrong! The number I'm thinking of is higher than {guess}.")
        elif guess > num:
            print(f"Wrong! The number I'm thinking of is lower than {guess}.")
        else:
            print("Correct!!!")
            is_num_guessed = True

    user_confirm = False
    while not user_confirm:
        selection = input("Would you like to play again? (Y/N): ")
        if selection.lower() == "y":
            is_num_guessed = False
            user_confirm = True
        elif selection.lower() == "n":
            is_running = False
            user_confirm = True
        else:
            print("Please enter a valid selection.")

