# DSC 510
# Week 8
# Programming Assignment Week 8.1
# Author Madhavi Ghanta
# 2/5/2023
"""
We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt.
(Click the link to download the text file).  Calculate the total words, and output the number of occurrences of each
word in the file.
Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
Nicely print the output, in this case from high to low frequency. You should use string formatting for this.
(See discussion 8.3).
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
We want to achieve each major goal with a function (one function, one action). We can find four functions that
need to be created.
add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
Process_line: There is some work to be done to process the line: strip off various characters, split out the words,
and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word.
No return value.
Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need
 to modify it later),we separated out the printing function. The parameter is a dictionary. No return value.
main: We will use a main function as the main program. As usual, it will open the file and call process_line on each
line. When finished, it will call pretty_print to print the dictionary.
In the main function, you will need to open the file. We will cover more regarding opening of files next week, but I
wanted to provide you with the block of code you will utilize to open the file, see below.
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


# Define main function
def main():
    # Open the file in read mode
    gba_file = open("gettysburg.txt", "r")
    # Create an empty dictionary
    word_dict = dict()
    # Call process_line and loop through each line of the file
    for line in gba_file:
        process_line(line, word_dict)
    gba_file.close()
    # Call pretty_print to print the dictionary
    pretty_print(word_dict, len(word_dict))


# Call to main function
if __name__ == '__main__':
    main()
