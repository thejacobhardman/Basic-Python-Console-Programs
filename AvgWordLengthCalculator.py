#################################################################################
#                     Lab 1 – A Python Program                                  #
#                                                                               #
# PROGRAMMER:        Jacob Hardman hard7293@bears.unco.edu                      #
# CLASS:             CS200                                                      #
# TERM:              Spring 2021                                                #
# INSTRUCTOR:        Dean Zeller                                                #
# SUBMISSION DATE:   1/15/2021                                                  #
#                                                                               #
# DESCRIPTION                                                                   #
# This program will calculate the average length of words based on user input.  #
#                                                                               #
# ORIGINAL SOURCE                                                               #
# This code was originally written by:                                          #
#    Author:   Jacob Hardman                                                    #
#    Location: https://github.com/thejacobhardman/Basic-Python-Console-Programs #
#                                                                               #
# COPYRIGHT:                                                                    #
# This program is copyright (c)2021 Jacob Hardman, and Dean Zeller              #
#                                                                               #
#################################################################################

import os, string

def cls(): ### I got this method to clear the console screen from StackOverflow.com: https://stackoverflow.com/a/684344
    os.system('cls' if os.name=='nt' else 'clear')

def Calculate_Avg_Word_Length(word_list):
    avg_length = 0

    for word in word_list:
        avg_length += len(word)

    return avg_length

is_running = True
while is_running:
    cls()

    print("Welcome to Average Word Length Calculator!")
    words = input("Please enter your list of words: ")

    exclude = set(string.punctuation) ### I got this code that is used to strip the punctuation from the string from StackOverflow.com: https://stackoverflow.com/a/266162
    words = ''.join(ch for ch in words if ch not in exclude) ### See above ^^^

    word_list = words.split()

    avg_length = Calculate_Avg_Word_Length(word_list) / len(word_list)

    print(f"You entered {len(word_list)} words. The average length of those words is {avg_length} letters.")

    user_confirm = False
    while not user_confirm:
        selection = input("Would you like to run the program again? (Y/N): ")
        if selection.lower() == "y":
            user_confirm = True
        elif selection.lower() == "n":
            user_confirm = True
            is_running = False
        else:
            print("Please enter a valid selection.")
