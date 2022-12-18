"""
Create a program with the following requirements:
Using comments, create a header at the top of the program indicating the purpose of the program,
assignment number, and your name. Refer to the submission instructions for an example of a header.
Display a welcome message for your user.
Retrieve the company name from the user.
Retrieve the number of feet of fiber optic cable to be installed from the user.
Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost,
 and total cost in a legible format.
Include appropriate comments throughout the program.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
"""

# DSC 510
# Week 2
# Programming Assignment Week 2.1
# Author Madhavi Ghanta
# 12/10/2022

import datetime

# Display a welcome message for your user.
print("Hello, Welcome to Cables Company!", "Hope you are having a good day!\n", sep="\n")

# Retrieve the company name from the user.
company_name = input("Please enter your company name : ")

# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Making sure user input is number
while True:
    try:
        num = float(input("Enter the number of feet of fiber optic cable needed:"))
        if num < 0:
            print("Enter a valid number")
        else:
            break
    except ValueError:
        print('Please enter a valid number.')

# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
calculated_cost = float(num) * 0.87
total_cost = round(calculated_cost, 2)

# Print a receipt for the user including the company name,
# number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
print("*************************************************")
print("*****************Company Receipt*****************")

print("Date/Time of service: " + str(datetime.datetime.now()))

print("Company Name : " + company_name)
print("Number of feet of fiber to be installed : " + str(num)+" feet")
print("Calculated cost : $", calculated_cost)
print("Total Cost :$", total_cost)
print("********** Thank you for your business!**********")
