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


def process_file(final_dict, file_name):
    # format printing
    print_structure = PrettyTable(['Word', 'Count'])
    counter_dict = 0

    for key, value in final_dict.items():
        print_structure.add_row([key, value])
        counter_dict = counter_dict + 1
    print(print_structure.get_string(sortby="Word"))

    with open(file_name, 'w') as w:
        w.write(str(print_structure.get_string(sortby="Word")))
        print("Length of dictionary :" + str(len(final_dict)))


def add_word(final_list, dict_para):
    # create dictionary
    create_dict: dict = {declare_dict: final_list.count(declare_dict) for declare_dict in final_list}
    # print(create_dict)
    # Identify the number of words in dictionary
    for word in create_dict:
        dict_para.append(word)


def process_line(read_file, dict_para):
    # Change the string to uppercase
    change_upper = read_file.upper()
    # Remove special characters
    remove_special_char = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", change_upper)
    # Create List
    create_list = list(remove_special_char.split(" "))
    # Remove empty strings
    final_list = ' '.join(create_list).split()
    add_word(final_list, dict_para)


def main():
    read_file = ""
    dict_para = []
    file_name = input("Enter the file name you would like the report to be saved: ")
    # Reading the text file
    try:
        gba_file = open('Gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
        # Remove space inbetween lines
    for line in gba_file:
        if not line.isspace():
            read_file = read_file + line
    process_line(read_file, dict_para)
    print("Length of the dictionary:" + str(len(dict_para)))
    final_dict: dict = {declare_dict: dict_para.count(declare_dict) for declare_dict in dict_para}
    process_file(final_dict, file_name)


# using special variable
if __name__ == "__main__":
    main()
