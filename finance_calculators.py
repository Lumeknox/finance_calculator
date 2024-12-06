# Pseudo code for finance calculator program:

"""
Start program
Import the math module.
Declare the variables for the while True function.
Use the while True function to have the user enter either 'investment' or 'bond'.
Based on their selection the program will either calculate investment return or bond payments.

If the user selected 'investment':
    Ask the user to input the following data: investment amount, interest rate and duration.
Ask the user to enter either 'simple' or 'compound' interest.
    Use the  A = P *(1 + r*t) formula for simple interest and A = P * math.pow((1+r),t) for compound.
Print the results.

If the user selected 'bond':
    Ask for the user to input te following data: house value, interest rate, bond duration.
Use the following formula to calculate bond repayments: repayment = (i * P)/(1 - (1 + i)**(-n))
Print the results.
End program
"""


# Import math module:

import math


# Implement a while True function to get the correct input until the right input has been entered.
# I had to lookup the 'while true' function here is the link: https://python-forum.io/thread-18971.html

while True:
    user_cal_choice = input("""
investment  -  to calculate the amount of interest you'll earn on your investment.
bond        -  to calculate the amount you'll have to pay on a home loan.
                                                       
Enter either 'investment' or 'bond' from the menu above to proceed:
                         \n""").lower().strip()
      
    if user_cal_choice in ("investment" , "bond"):

        break
    
    else:
        print("\nInput Error - please enter either 'investment' or 'bond' to proceed:\n".upper())


# If the user selected 'investment' then ask the user a series of information to calculate the investment return:

if user_cal_choice == "investment":
    while True:
        try:
            invest_amount = float(input("How much can you deposit?\n"))
            invest_int = float(input("What is your preferred interest rate?\n"))
            invest_dur = int(input("What is your desired investment period in years?\n"))

            break

        except ValueError:
             print("\nInput error - please enter a number.".upper())


    while True:
        int_type = input("Enter whether you prefer 'simple' or 'compound' interest:\n").lower().strip()
        if int_type in ("simple", "compound"):

            break

        else:
            print("\nInput error - please enter either 'simple' or 'compound'.".upper())


# Simple and compound interest formula:

    total_simp_int = round(invest_amount * (1 + ((invest_int / 100) * invest_dur)), 2)
    total_comp_int = round(invest_amount * math.pow((1 + (invest_int / 100)) , invest_dur), 2)

 
# Print the results based on the choices made by the user:

    if int_type == "simple":
       print(f"""
Total investment return based on:
Amount: R{invest_amount}
Interest rate: {invest_int}%
Interest type: {int_type}
Duration: {invest_dur} year/s
Is: R{total_simp_int}
           """)

    else:
        print(f"""
Total investment return based on:
Amount: R{invest_amount}
Interest rate: {invest_int}%
Interest type: {int_type}
Duration: {invest_dur} year/s
Is: R{total_comp_int}
           """) 


# If the user chose 'bond' at the start of the program, ask the user for the relevant data needed to calculate repayments.
# Ask the user to input the necessary values to calculate the bond payments.

else:

    while True:
        try:
            house_val = float(input("What is the value of the house?\n"))
            bond_int = float(input("What is your preferred interest rate?\n"))
            bond_dur = int(input("What is your preferred bond repayment period in months?\n"))

            break

        except ValueError:
            print("\nInput error - please enter a number.".upper())


# Bond formula:

    bond_repay = round((((bond_int / 100) / 12) * house_val) / (1 - (1 + (bond_int / 100) / 12)**(-bond_dur)), 2)


# Print the results based on the choices made by the user:

    print(f"""
Your monthly bond repayment based on:
House value: R{house_val}
Interest rate: {bond_int}%
Bond repayment period: {bond_dur} months
Is: R{bond_repay}
        """)
