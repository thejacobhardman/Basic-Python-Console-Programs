################################################################################
#                     Lab 1 – A Python Program                                 #
#                                                                              #
# PROGRAMMER:        [your name] [your email address]                          #
# CLASS:             [CS160 or CS200]                                          #
# TERM:              Spring 2021                                               #
# INSTRUCTOR:                                                      #
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

is_running = True

while is_running:
    conversion = ""

    print("Welcome to Temperature Converter!")

    print("1: Celsius to Fahrenheit \n2: Fahrenheit to Celsius")

    user_confirm = False
    while not user_confirm:
        selection = input("Please select which conversion you would like to perform: ")

        if int(selection) == 1:
            conversion = "celsius"
            user_confirm = True
        elif int(selection) == 2:
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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
