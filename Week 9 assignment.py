# DSC 510
# Week 9
# Programming Assignment Week 9
# Author: Reenie Christudass
# 05/15/2022

# Change#:1
# Change(s) Made: Create dictionary and print in text file
# Date of Change: 05/15/2022
# Author: Reenie Christudass
# Change Approved by: Michael Eller
# Date Moved to Production: 05/15/2022

# import Regex pattern
import re
# import pretty table
from prettytable import PrettyTable


def process_file(Unique_dict, filename):
    # format printing
    print_structure = PrettyTable(['Word', 'Count'])
    counter_dict = 0
    for key, value in Unique_dict.items():
        print_structure.add_row([key, value])
        counter_dict = counter_dict + 1
    print(print_structure.get_string(sortby="Count", reversesort=True))

    # create file
    with open(filename, 'w') as w:
        w.write(str(print_structure.get_string(sortby="Count", reversesort=True)))
        w.write("\n")
        w.write("Total Number of Unique Words or Length of dictionary: " + str(len(Unique_dict)))


def add_word(final_list, word_dict):
    for word in final_list:
        # print(word)
        if word != "":
            word_dict.append(word)


def process_line(current_line, word_dict):
    create_list = []
    # Change the string to uppercase
    line = current_line.upper()
    # Remove special characters
    line = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", line)
    # Remove \n
    line = line.replace('\n', "")
    # Create List
    create_list = list(line.split(" "))
    add_word(create_list, word_dict)


def main():
    read_file = ""
    word_dict = []

    # Reading the text file
    file_name = input("Enter the file name you would like the report to be saved: ")
    try:
        gba_file = open('Gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
        # Remove space inbetween lines
    for line in gba_file:
        if not line.isspace():
            # read_file = line
            process_line(line, word_dict)
            # print(line)
    unique_dict: dict = {declare_dict: word_dict.count(declare_dict) for declare_dict in word_dict}

    print("Length of the dictionary:" + str(len(unique_dict)))
    process_file(unique_dict, file_name)


# using special variable
if __name__ == "__main__":
    main()
