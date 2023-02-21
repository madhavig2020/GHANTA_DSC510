# DSC 510
# Week 10
# Programming Assignment Week 10.1
# Assignment to get data from API & parse the value
# Author Madhavi Ghanta
# 2/18/2023
"""
Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to
obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make
sure that your program does error checking at this point. If you ask user to enter “Y” and they enter y, is that ok?
Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about included
string functions you might be able to call.
Your program must include a header as in previous weeks.
Your program must have a properly defined main method and a properly defined call to main.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
Your program must include a welcome message for the user.
Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context does not
represent “pretty.”
"""

import requests
import json


# function to get Joke -  will call API and get the values in JSON and display only value

def get_joke():
    user_input = 'Y'
    input_msg_txt = 'Do you wish to read a Science Joke? Type Y or N then press enter.\n'

    while user_input.upper() == 'Y':
        user_input = input(input_msg_txt)
        try:
            # get the API value into response
            response = requests.get("https://api.chucknorris.io/jokes/random?category=science")
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print("Error")
            raise err
            # error handling API call
        if response.status_code != 200:
            print("Connection  unsuccessful. Please try again after sometime.")
        elif user_input.upper() == 'Y':
            response_json = json.loads(response.text)
            joke_text = (response_json['value'])
            pretty_print(joke_text)
        elif user_input.upper() == 'N':
            print("Thank you. Have a great day!")
        else:
            print("Invalid Entry, Please try again")
            get_joke()


# function to print joke

def pretty_print(joke):
    print('--------This is your joke----------')
    print(joke)
    print('--------End of joke--------------')


# main function to call get Joke


def main():
    # Display Welcome message for user
    print("Welcome to Chuck Norris Science Jokes!")
    # call get_joke function to get Joke and print
    get_joke()


# To call main function

if __name__ == '__main__':
    main()
