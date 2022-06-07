# DSC 510
# Week 11
# Programming Assignment Week 11
# Author: Reenie Christudass
# 05/23/2022

# Change#:1
# Change(s) Made: Cash register program
# Date of Change: 05/23/2022
# Author: Reenie Christudass
# Change Approved by: Michael Eller
# Date Moved to Production: 05/23/2022

import locale
from termcolor import colored

locale.setlocale(locale.LC_ALL, 'en_US')


class CashRegister:

    # constructor
    def __init__(self):
        self.total = 0.0
        self.itemCount = 0

    # setter
    def add_item(self, price):
        self.total = self.total + float(price)
        self.itemCount = self.itemCount + 1

    # getter
    def get_total(self):
        return self.total

    def get_count(self):
        return self.itemCount


def process_line(create_list):
    print("")
    print("---------------THANK YOU FOR USING CASH REGISTER---------------------------")
    print("")
    # Print all items purchased
    if create_list:
        for n in range(len(create_list)):
            text = colored(create_list[n], 'blue')
            print("Item Purchased " + str(n + 1) + ":" + '$ ' + text)
    else:
        print("")
        print("No items selected")


def main():
    print("WELCOME TO CASH REGISTER!!!!")
    register = CashRegister()
    create_list = []
    # variable declared to have the program in loop unless exited by the user
    item_loop = 0
    while item_loop >= 0:
        # Allow user to enter the price of the item
        if item_loop == 0:
            input_message = input("Enter the price of the item or enter exit to quit the program:")
        elif item_loop > 0:
            input_message = input("Enter the price of another item or enter exit to quit the program:")
        # read the file

        if input_message != 'exit':
            try:
                # program will convert the user input value to float
                input_message = float(input_message)
                create_list.append(input_message)
            except ValueError as e:
                # if the program couldn't convert the value to float , it will prompt the user to enter value in numeric
                print("Please enter the numeric value for item")
                continue

            register.add_item(input_message)
        # if the user input is equal to exit
        elif input_message == 'exit':
            break
        print()
        item_loop = item_loop + 1
    process_line(create_list)

    print("")
    message_output = ("Total Cost of the items purchased : {}".format(locale.currency(register.get_total())))
    print(colored(message_output, 'yellow'))
    message_output = ("Total Items Purchased: {}".format(colored(register.get_count()), 'blue'))
    print(colored(message_output, 'magenta'))
    print("")
    print("Thank you and have a great day")


# using special variable
if __name__ == "__main__":
    main()
