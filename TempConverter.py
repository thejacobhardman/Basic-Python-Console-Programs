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
# This program will convert a temperature value in either Celsius or Fahrenheit #
# to the opposite temperature scale.                                            # 
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

import os

def cls(): ### I got this method to clear the console screen from StackOverflow.com: https://stackoverflow.com/a/684344
    os.system('cls' if os.name=='nt' else 'clear')

is_running = True

while is_running:
    cls()
    conversion = ""

    print("Welcome to Temperature Converter!")

    print("1: Celsius to Fahrenheit \n2: Fahrenheit to Celsius")

    user_confirm = False
    while not user_confirm:
        selection = input("Please select which conversion you would like to perform: ")

        if selection == "1":
            conversion = "celsius"
            user_confirm = True
        elif selection == "2":
            conversion = "fahrenheit"
            user_confirm = True
        else:
            print("Please enter a valid selection.")

    temp = input("Please enter the value of the temperature that you'd like to convert as an integer: ")

    if conversion == "celsius":
        converted_temp = ((int(temp) * 9/5) + 32)
        print(str(temp) + " C° is " + str(converted_temp) + " F°.")
    elif conversion == "fahrenheit":
        converted_temp = ((int(temp) - 32) * 5/9)
        print(str(temp) + " F° is " + str(converted_temp) + " C°.")
    
    input("Please press any button to continue.")
