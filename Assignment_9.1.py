# DSC 510
# Week 9
# Programming Assignment Week 9.1
# Change(s) Made: Added function process_file to print to file input lines 66-78 added
# Author Madhavi Ghanta
# 2/11/2023
"""
Last week we got a taste of working with files. This week we’ll really dive into files by opening and closing
files properly.
For this week we will modify our Gettysburg processing program from week 8 in order to generate a text file from the
output rather than printing to the screen. Your program should have a new function called process_file which prints
to the file (this method should almost be the same as the pretty_print function from last week). Keep in mind that we
have print statements in main as well. Your program must modify the print statements from main
as well.
Your program must have a header.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8
however it will print to a file instead of to the screen.
Modify your main method to print the length of the dictionary to the file as opposed to the screen.
This will require that you open the file twice. Once in main and once in process_file.
Prompt the user for the filename they wish to use to generate the report.
Use the filename specified by the user to write the file.
This will require you to pass the file as an additional parameter to your new process_file function.
"""
import string


def process_line(line, word_dict):
    # Remove the leading spaces and newline character
    line = line.strip()
    # Convert the characters in line to lowercase to avoid case mismatch
    line = line.lower()
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Split the line into words
    words = line.split(" ")
    add_word(words, word_dict)


def add_word(words, word_dict):
    for word in words:
        if word != "":
            # Check if the word is already in dictionary
            if word in word_dict:
                # Increment count of word by 1
                word_dict[word] = word_dict[word] + 1
            else:
                # Add the word to dictionary with count 1
                word_dict[word] = 1


"""
# Print the contents of dictionary
def pretty_print(word_dict, word_num):
    # Print the contents of dictionary
    print('Length of the dictionary :', len(word_dict))
    print("{:<20} {:<15} ".format('Word', 'Count'))
    print("---------------------------")
    # for key in list((d.keys())):
    for key in sorted(word_dict, key=word_dict.get, reverse=True):
        # print(key, ":", d[key])
        print("{:<20} {:<15} ".format(key, word_dict[key]))
"""


# Print the contents of dictionary
def process_file(word_dict, output_filename):
    # Print the contents of dictionary
    output_file = open(output_filename, "w")  # write mode
    output_file.write("---------------------------" + "\n")
    output_file.write("---------------------------" + "\n")
    output_file.write("{:<20} {:<15} ".format('Word', 'Count') + "\n")
    output_file.write("---------------------------" + "\n")

    for key in sorted(word_dict, key=word_dict.get, reverse=True):
        # print("{:<20} {:<15} ".format(key, word_dict[key]))
        output_file.write("{:<20} {:<15} ".format(key, word_dict[key]) + "\n")
    output_file.close()


# Define main function
def main():
    # Receive the file name to write the output
    output_filename = input("enter your output file name :")
    # Open the file in read mode
    input_file = open("gettysburg.txt", "r")
    # Create an empty dictionary
    word_dict = dict()
    # Call process_line and loop through each line of the file
    for line in input_file:
        process_line(line, word_dict)
    input_file.close()
    # Write the length of the dict in the output file
    output_file = open(output_filename, "w")  # write mode
    output_file.write('Length of the dictionary :' + str(len(word_dict)) + "\n")
    # call the process file method by passing dict, filename to print the words and length of dict
    process_file(word_dict, output_filename)
    print("The output is printed in the file.Thanks!")


# Call to main function
if __name__ == '__main__':
    main()
