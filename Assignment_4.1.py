"""
This week we will modify our IF Statement program to add a function to do the heavy lifting.
Modify your IF Statement program to add a function. This function will perform the cost calculation.
The function will have two parameters (feet and price). When you call the function, you will pass two
arguments to the function; feet of fiber to be installed and the cost (remember that price is dependent on the number
of   feet being installed). You should have the following:
Your program must have a header.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
A welcome message.
A function with two parameters.
A call to the function.
The application should calculate the cost based upon the number of feet being ordered.
A printed message displaying the company name and the total calculated cost.
All costs should display in USD Currency Format Ex: $123.45.
Your program must have a properly defined main method and a properly defined call to main.
"""
# DSC 510
# Week 4
# Programming Assignment Week 4.1
# Author Madhavi Ghanta
# 1/7/2023

# Change#:2
# Change(s) Made: Added main function, welcome , user_input ,installation rate,total_cost functions
# Date of Change: 1/7/2023
# Author: Madhavi Ghanta
# Change Approved by: Michael Eller

import datetime


def welcome():
    # Display a welcome message for your user.
    print("Hello, Welcome to Cables Company!", "Hope you are having a good day!\n", sep="\n")


def user_input():
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
    return cable_length


def installation_rate(cable_length):
    # calculate bulk discount
    # > 100 feet = 0.80
    # > 250 feet = 0.70
    # > 500 feel = 0.50100

    # If the user purchases more than 100 feet they are charged $0.80 per foot.
    if 100 < cable_length <= 250:
        price = 0.80
    # If the user purchases more than 250 feet they will be charged $0.70 per foot.
    elif 250 < cable_length <= 500:
        price = 0.70
    # If they purchase more than 500 feet, they will be charged $0.50 per foot.
    elif cable_length > 500:
        price = 0.50
    else:
        price = 0.87
    return price


def total_cost(cable_length, price):
    # This function will calculate the total cost
    installation_cost = float(cable_length) * price
    return round(installation_cost, 2)


def main():
    welcome()
    # Retrieve the company name from the user.
    company_name = input("Please enter your company name : ")
    print('Thank you', company_name, 'for calling the Fiber Optic')
    cable_length = user_input()
    price = installation_rate(cable_length)
    total_installation_cost = total_cost(cable_length, price)
    print_receipt(company_name, cable_length, total_installation_cost)


def print_receipt(company_name, cable_length, total_installation_cost):
    # This function will print the customer receipt
    # Print a receipt for the user including the company name,
    # number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
    print("*************************************************")
    print("*****************Company Receipt*****************")
    print("Date/Time of service: " + str(datetime.datetime.now()))
    print("Company Name : " + company_name)
    print("Number of feet of fiber to be installed : " + str(cable_length) + " feet")
    print("Total installation Cost :$", total_installation_cost)
    print("********** Thank you for your business!**********")


if __name__ == '__main__':
    main()
    
