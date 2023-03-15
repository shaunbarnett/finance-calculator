# program that allows the user to access two
# different financial calculators: an investment calculator and a home loan
# repayment calculator.

import math

# Welcome message explaining the types of payment calculator
# Asking user to enter which type of investment they would like

print("PLease choose which calculation you require")
print("Choose either 'investment' or 'bond'. Description below.\n")
print("investment   -   to calculate the amount of interest you will earn on your investment.")
print("bond         -   to calculate the amount you will have to pay on a home loan.\n")

calculation = input("Please enter your choice: ").lower()

# if user enters investment, they are asked to give details and decide
# between simple and compound

if calculation == "investment":
    deposit = float(input("How much would you like to deposit?: "))
    interest_rate = float(input("what is your interest rate? enter a number: "))
    years = int(input("How many years do you plan on investing?: "))
    interest = input("what interest would you like? 'compound' or 'simple': ").lower()

# There are two calculations below depending on whether the user picks simple or compound investment

    if interest == "simple":
        interest_rate /= 100
        total = deposit * (1 + interest_rate * years)
        print("Your total investment after", years, "years will be", round(total))
    elif interest == "compound":
        interest_rate /= 100
        total = deposit * math.pow((1 + interest_rate), years)
        print("Your total investment after", years, "years will be", round(total))
    else:
        print("You have entered incorrectly. Enter 'simple' or 'compound'. ")

# calculations for bond if chosen by users

elif calculation == "bond":
    house_value = int(input("what is the present value of your house?: "))
    interest_rate = int(input("What is your interest rate? Please enter a number: "))
    months = int(input("Please enter the number of months you would like to repay the loan:  "))
    interest_rate /= 100 / 12
    repayment = house_value / months * interest_rate

    print("Your monthly repayments for this loan will be", repayment)

# an else just in case none of the above conditions are met

else:
    print("You have entered incorrectly. Enter 'investment' or 'bond'")








