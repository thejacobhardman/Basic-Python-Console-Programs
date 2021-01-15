################################################################################
#                     Lab 1 – A Python Program                                 #
#                                                                              #
# PROGRAMMER:        [your name] [your email address]                          #
# CLASS:             [CS160 or CS200]                                          #
# TERM:              Spring 2021                                               #
# INSTRUCTOR:                                                     #
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
#                                                                  #
#                                                                              #
################################################################################

import os

def cls():
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
