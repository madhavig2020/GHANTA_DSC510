"""
This week we will implement “if statements” in a program. Your program will calculate the
cost of fiber optic cable installation by multiplying the number of feet needed by $0.87.
We will also evaluate a bulk discount. You will prompt the user for the number of fiber optic cable
they need installed. Using the default value of $0.87 calculate the total expense. If the user
purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than
250 feet they will be charged $0.70 per foot. If they purchase more than 500 feet, they will be
charged $0.50 per foot.
Your program must have a header. See below for an example of what must be included with each
assignment.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
Display a welcome message for your program.
Get the company name from the user.
Get the number of feet of fiber optic cable to be installed from the user.
Evaluate the total cost based upon the number of feet requested.
Display the calculated information including the number of feet requested and company name.
"""
# DSC 510
# Week 2
# Programming Assignment Week 3.1
# Author Madhavi Ghanta
# 12/13/2022

# Change#:1
# Change(s) Made: Added if else condition to calculate discount  input lines 56-67 added
# Date of Change: 12/17/2022
# Author: Madhavi Ghanta
# Change Approved by: Michael Eller


import datetime

# Display a welcome message for your user.
print("Hello, Welcome to Cables Company!", "Hope you are having a good day!\n", sep="\n")

# Retrieve the company name from the user.
company_name = input("Please enter your company name : ")

# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Making sure user input is number
while True:
    try:
        cable_length = float(input("Enter the number of feet of fiber optic cable needed:"))
        if cable_length < 0:
            print("Enter a valid number")
        else:
            break
    except ValueError:
        print('Please enter a valid number.')

# calculate bulk discount
# > 100 feet = 0.80
# > 250 feet = 0.70
# > 500 feel = 0.50100
installation_cost = 0
if cable_length <= 100:
    installation_cost = float(cable_length) * 0.87

# If the user purchases more than 100 feet they are charged $0.80 per foot.
if 100 < cable_length <= 250:
    installation_cost = float(cable_length) * 0.80
# If the user purchases more than 250 feet they will be charged $0.70 per foot.
elif 250 < cable_length <= 500:
    installation_cost = float(cable_length) * 0.70
# If they purchase more than 500 feet, they will be charged $0.50 per foot.
elif cable_length > 500:
    installation_cost = float(cable_length) * 0.50

total_cost = round(installation_cost, 2)
# Print a receipt for the user including the company name,
# number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
print("*************************************************")
print("*****************Company Receipt*****************")

print("Date/Time of service: " + str(datetime.datetime.now()))

print("Company Name : " + company_name)
print("Number of feet of fiber to be installed : " + str(cable_length)+" feet")
print("Installation cost : $", installation_cost)
print("Total Cost :$", total_cost)
print("********** Thank you for your business!**********")
