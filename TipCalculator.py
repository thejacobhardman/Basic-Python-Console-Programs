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
# This program will calculate the correct tip amount based on the original      #
# value of the bill.                                                            # 
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

def Calculate_Tip(money_paid, tip_percent):
    return money_paid * (tip_percent * 0.01)

is_running = True
while is_running:
    cls()
    print("Welcome To Tip Calculator!")

    tip_amount = Calculate_Tip(money_paid=float(input("Please enter the amount of money that you paid as a decimal: ")), 
                               tip_percent=float(input("Please enter the amount that you would like to tip as an integer. (10 = 10%): ")))

    print("You've tipped $" + str(round(tip_amount, 2)) + ".")
    input("Press any key to continue.")
