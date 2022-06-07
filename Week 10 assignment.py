# DSC 510
# Week 10
# Programming Assignment Week 10
# Author: Reenie Christudass
# 05/18/2022

# Change#:1
# Change(s) Made: Web services
# Date of Change: 05/18/2022
# Author: Reenie Christudass
# Change Approved by: Michael Eller
# Date Moved to Production: 05/18/2022

import requests
from termcolor import colored


def process_line(receive_joke):
    # Print the joke
    if receive_joke:
        print("")
        print("---------------THANK YOU FOR PLAYING READ JOKE---------------------------")
        print("")
        print("You requested a total of " + str(len(receive_joke)) + " " + "Joke")
        print("")
        print("LIST OF JOKES....")
        for n in range(len(receive_joke)):
            receive_joke[n] = receive_joke[n].upper()
            text = colored(receive_joke[n], 'blue')
            print("Joke " + str(n + 1) + ":" + text)
    else:
        print("")
        print("No Jokes selected")


def main():
    print("WELCOME TO READ JOKES!!!!")
    receive_joke = []
    # variable declared to have the program in loop unless exited by the user
    item_loop = 0
    # variable declared to count how many times user want to view a joke
    # counter_loop = 0
    while item_loop >= 0:
        # identify if the user want to view Chuck Norris Joke
        if item_loop == 0:
            input_message = input("Would you like to read Chuck Norris Joke Y or N:")
        elif item_loop > 0:
            input_message = input("Would you like to another Chuck Norris Joke Y or N:")
        # read the file
        try:
            response = requests.get("https://api.chucknorris.io/jokes/random")
            jokes = response.json()
            joke_list = jokes['value']
        except ValueError as e:
            print("No value read")
        # validate the user input
        if input_message == 'N':
            break
        elif input_message == 'Y':
            receive_joke.append(joke_list)
            print(joke_list)
        elif input_message.isnumeric():
            message_output = "Your input {} is not a valid option. Please select a valid option Y or N".format(
                input_message)
            text_color = colored(message_output, 'yellow')
            print(text_color)
        elif input_message.upper() != 'Y' or input_message.upper() != 'N':
            message_output = "Your input {} is not valid option. Please select a valid option Y or N".format(
                input_message)
            text_color = colored(message_output, 'magenta')
            print(text_color)

            item_loop = item_loop + 1
    process_line(receive_joke)
    print("")
    print("Thank you. Good Bye!!!")


# using special variable
if __name__ == "__main__":
    main()
