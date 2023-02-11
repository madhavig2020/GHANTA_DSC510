# DSC 510
# Week 6
# Programming Assignment Week 6.1
# Author Madhavi Ghanta
# 1/21/2023
"""
This week we will create a program which works with lists. Your goal is to create a program which contains
 a list of temperatures. Your program will populate the list based upon user input.
Your program will determine the number of temperatures in the program, determine the largest
temperature, and the smallest temperature.
Your program must have a header.
Your program must have a properly defined main method and a properly defined call to main.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
Create an empty list called temperatures.
Allow the user to input a series of temperatures along with a sentinel value (do not use a number for a sentinel value)
 which will stop the user input.
Evaluate the temperature list to determine the largest and smallest temperature.
Print the largest temperature.
Print the smallest temperature.
Print a message that tells the user how many temperatures are in the list.
"""
def main():
    # Create an empty list
    temperatures = []
    # Accept user inputs and move them into list
    accept_user_inputs(temperatures)
    # Print results
    print_results(temperatures)


def accept_user_inputs(temperatures):
    temp = 0
    while temp != "q" or temp != "Q":
        while True:
            temp = input("Enter the temperature, use q to stop: \n")
            try:
                temp = int(temp)
                break
            except ValueError:
                try:
                    temp = float(temp)
                    break
                except ValueError:
                    if temp.upper() == "Q":
                        break

                    print("Please check and enter a valid temperature!\n")
        # Break out of the loop, when user inputs "Q" or "q"
        if temp == "q" or temp == "Q":
            break
        temperatures.append(temp)


def print_results(temperatures):
    # Find min & max of the temperatures list#
    print("Largest temperature entered by the user is", str(max(temperatures)))
    print("Smallest temperature entered by the user is", str(min(temperatures)))
    print("Total count of temperature inputs in the list is", str(len(temperatures)))


if __name__ == '__main__':
    main()
