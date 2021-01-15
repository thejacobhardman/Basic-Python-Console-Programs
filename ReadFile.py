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

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

file = open("words.txt", "r")

def Filter_Word_List(letter):
    filtered_word_list = []
    for line in file:
        if letter == list(line)[0]:
            word = line[:-2] #removing the \n characters from the word
            filtered_word_list.append(word)
    
    return filtered_word_list

is_running = True
while is_running:
    cls()
    print("Welcome! \nAttached to this program is a .txt file with nearly every word in the English language!")

    letter = input("Enter a letter and I will show you how many words in English start with that letter: ")

    filtered_list = Filter_Word_List(letter)
    num_of_words = len(filtered_list)

    print(f"There are {num_of_words} words that start with the letter {letter}.")

    user_confirm = False
    while not user_confirm:
        selection = input("Would you like to see a list of the words? (Y/N):")
        if selection.lower() == "y":
            print(filtered_list)
            user_confirm = True
        elif selection.lower() == "n":
            user_confirm = True
        else:
            print("Please enter a valid selection.")

    user_confirm = False
    while not user_confirm:
        selection = input("Would you like to run the program again? (Y/N):")
        if selection.lower() == "y":
            user_confirm = True
        elif selection.lower() == "n":
            user_confirm = True
            is_running = False
        else:
            print("Please enter a valid selection.")

    input("Press any button to continue.")

file.close()
