"""
Your program must have a header.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
This program will perform various calculations (addition, subtraction, multiplication, division,and average calculation)
This program will contain a variety of loops and functions.
The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the
 user.
Define a function named performCalculation which takes one parameter. The parameter will be the operation being
performed (+, -, *, /).
This function will perform the given prompt the user for two numbers then perform the expected operation depending on
the parameter that's passed into the function.
This function will print the calculated value for the end user.
Define a function named calculateAverage which takes no parameters.
This function will ask the user how many numbers they wish to input.
This function will use the number of times to run the program within a for loop in order to calculate the total and
average.
This function will print the calculated average.
This program will have a main method which contains a while loop. The while loop will be used to allow the user to run
the program until they enter a value which ends the loop.
The main method should prompt the user for the operation they wish to perform.
The main method should evaluate the entered data using if statements.
The main method should call the necessary function to perform the calculation.
"""
# DSC 510
# Week 5
# Programming Assignment Week 5.1
# Author Madhavi Ghanta
# 1/15/2023
def getResponse():
    """
    This function asks user if they want to continue with the program
    """
    response = input('Would you like to continue? "y" or "n"')
    # give the user 5 times to input correct response before ending the program
    for i in range(5):
        # If user enters n, the program will end and print thank you!
        if response == "n":
            print("Thank You!")
            return False
        # If user enters y, the program continue to operator selection menu
        elif response == "y":
            return True
        # If user enters other than y or n, the program reiterates
        else:
            response = input('Please enter "y" or "n"')
            continue


def getOperator():
    """
    This function asks user to choose an operation to perform and returns the operator
    """
    operators = ['+', '-', '*', '/', 'avg']
    while True:
        print("Enter one of the following:")
        print("+ = Addition")
        print("- = Subtraction")
        print("* = Multiplication")
        print("/ = Division")
        print("avg = Average")
        Input_operator = input()
        if Input_operator in operators:
            return Input_operator
        else:
            continue


def performCalculation(operator):
    """
    This function first prompts the user to input two numbers
    Then perform the arithmetic operation depending on the chosen operator passed into the function.
    At the end of the operation, function will print the calculated value (result) for the user.
    :param operator: Operator from +, -, *, /
    """
    Number1 = float(input('Enter First Number: \n'))  # Input first number
    Number2 = float(input('Enter Second Number: \n'))  # Input second number
    while True:
        # If operator is +, the 2 numbers will be added
        if operator == "+":
            result = Number1 + Number2
            print("Result =", round(result, 2))
        # If operator is -, the 2 numbers will be subtracted
        elif operator == "-":
            result = Number1 - Number2
            print("Result =", round(result, 2))
        # If operator is *, the 2 numbers will be multiplied
        elif operator == "*":
            result = Number1 * Number2
            print("Result =", round(result, 2))
        # If operator is /, the 2 numbers will be divided
        elif operator == "/":
            result = Number1 / Number2
            print("Result =", round(result, 2))
        return

def calculateAverage():
    """
    This function calculates the average for total numbers inputted by the user
    """
    print("Let's calculate the average for total numbers entered")
    while True:
        try:
            # Prompts user to input total numbers for the list
            count = int(input('How many numbers do you want to enter: \n'))
            # Will tell user to enter number a different number greater than 0, if user enters a 0
            if count == 0:
                print("Enter number greater than 0")
                continue
            break
            # Prompts user to enter an integer only
        except ValueError:
            print("Not an integer, try again!")
    sum_number = 0
    for i in range(0, count):  # for loop where input_number = total numbers entered
        input_number = float(input('Enter Number: \n'))  # Enter each number for the list of numbers
        sum_number = sum_number + input_number  # Calculates sum here
    average = sum_number / count  # Calculates average
    # Prints sum and average of the total numbers entered, round to 2 decimal places
    print("Sum total numbers entered =", round(sum_number, 2))
    print("Average of total numbers entered =", round(average, 2))


def main():
    """
    This function is used to start the main menu of the program
    and asks user if the user want to continue or end the program
    """
    response = True
    while response:
        operation = getOperator()
        # If operation is chosen as avg (average), this will calculate average
        if operation == "avg":
            calculateAverage()
        # Any other chosen operators, will perform the basic arithmetic operation calculation
        else:
            performCalculation(operation)
        response = getResponse()

if __name__ == "__main__":
    main()
    
