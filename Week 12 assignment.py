# DSC 510
# Week 12
# Programming Assignment Week 12
# Author: Reenie Christudass
# 06/4/2022

# Change#:1
# Change(s) Made: web services program
# Date of Change: 06/04/2022
# Author: Reenie Christudass
# Change Approved by: Michael Eller
# Date Moved to Production: 06/04/2022

# api call request
import requests
# color parameters
from termcolor import colored


def get_weather(name, latitude, longitude):
    # receive input from user to check to view the temperature in Kelvin, Fahrenheit, celsius
    # the loop will check three times before exiting the program
    loop_check = 0
    temp_code_unit = " "
    temp_code = ""
    while loop_check < 3:
        loop_check = loop_check + 1
        print("")
        print(colored("Would you like to see the weather details in:", 'blue'))
        print("1 - Kelvin")
        print("2 - Fahrenheit")
        print("3 - Celsius")
        print("")
        temp_code = input("Select your metric option:")
        # if user select "1" , display the temperature in Kelvin
        if temp_code == "1":
            temp_code_unit = "standard"
            break
        # if user select "2" , display the temperature in Fahrenheit
        elif temp_code == "2":
            temp_code_unit = "imperial"
            break
        # if user select "3" , display the temperature in Celsius
        elif temp_code == "3":
            temp_code_unit = "metric"
            break
        else:
            print(" ")
            print("{} is not the metric".format(colored(temp_code, 'green')))
            # if user selected an option other than 1, 2 or 3 , request the user to input the value again
            # after three attempts, user is provided a different option
            if loop_check == 3:
                print(" ")
                print("You have entered an invalid option three time.Lets try again with a different value!")
                break
    # display weather details
    if temp_code == "1" or temp_code == "2" or temp_code == "3":
        API_KEY = "987c588aeadb760cdde052ca8a79731f"
        weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&units=" \
                      f"{temp_code_unit}&exclude=hourly,minutely&appid={API_KEY}"

        # api call request
        try:
            get_weather_data = requests.get(weather_url).json()
            response = requests.get(weather_url)
            response.raise_for_status()
        # api call failure
        except requests.exceptions.HTTPError:
            #print("Error Connecting:", e.errno)
            print("The entered request {} does not exist.".format(colored(name, 'blue')))
        # api call is success get the data
        else:
            # print the weather conditions
            print("")
            print(colored(("Current weather condition for " + str(name)), 'yellow'))
            print("-------------------------------------------")
            print("Current temperature for the day :" + colored(
                str(get_weather_data['current']['temp']) + str(" degrees"),
                'yellow'))
            print("Current pressure :" + colored(str(get_weather_data['current']['pressure']) + str("hPa"), 'yellow'))
            print("Current humidity :" + colored(str(get_weather_data['current']['humidity']) + str("%"), 'yellow'))
            print(
                "Current weather description :" + colored(str(get_weather_data['current']['weather'][0]["description"]),
                                                          'yellow'))
            print("Forecast Minimum temperature:" + colored(
                str(get_weather_data['daily'][0]['temp']['min']) + str(" degrees"), 'yellow'))
            print("Forecast Maximum temperature:" + colored(
                str(get_weather_data['daily'][0]['temp']['max']) + str(" degrees"), 'yellow'))
            print("")


def get_zipcode():
    # receive the input (zipcode) from user
    loop_check = 0
    while loop_check < 3:
        loop_check = loop_check + 1
        # receive the input (zipcode) from user
        zipcode = input("Enter the zipcode:")
        # check if the user input is numeric and length 5
        if zipcode.isnumeric():
            if len(zipcode) == 5:
                # if the entered zipcode is numeric and length 5, go to function
                get_weather_by_zipcode(zipcode)
                break
            else:
                print("You have entered an invalid zipcode.")
        # if the user input is not numeric for zipcode
        # after failed three attempt, the program will start again
        else:
            print("You have entered an invalid zipcode.")
            if loop_check == 3:
                print("You had 3 incorrect attempts. Lets try again with a different value!")


def get_weather_by_zipcode(zipcode):
    # hard coded to country US
    country_code = "US"
    API_KEY = "987c588aeadb760cdde052ca8a79731f"
    location_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country_code}&appid={API_KEY}"
    # check the status of the api call
    try:
        zip_code_data = requests.get(location_url).json()
        response = requests.get(location_url)
        response.raise_for_status()
    # api call failure will be received in variable e
    except requests.exceptions.HTTPError:
        # print("Error Connecting:", e)
        print("The entered zipcode {} does not exist.".format(colored(zipcode, 'blue')))
    # api call is success get the data from list dictionary
    else:
        name = zip_code_data['name']
        latitude = zip_code_data['lat']
        longitude = zip_code_data['lon']
        get_weather(name, latitude, longitude)


def get_city_name():
    limit = "5"
    city_name = input("Enter the city name in US:")
    country_code = "US"
    API_KEY = "987c588aeadb760cdde052ca8a79731f"
    city_name_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}" \
                    f"&appid={API_KEY}"
    # check the status of the api call
    try:
        city_name_data = requests.get(city_name_url).json()
        response = requests.get(city_name_url)
        response.raise_for_status()
    # api call failure will be received in variable e
    except requests.exceptions.HTTPError:
        print(" ")
        print("The entered zipcode {} does not exist.".format(colored(city_name, 'blue')))
    # api call is success get the data from list dictionary
    else:
        create_list = [f['state'] for f in city_name_data]
        create_list = list(set(create_list))
        create_list.sort()
        # based on the user input for the "City name", gather all the states under it
        # if the user input has only one city and one state association
        if len(create_list) == 1:
            name = city_name_data[0]['name']
            latitude = city_name_data[0]['lat']
            longitude = city_name_data[0]['lon']
            get_weather(name, latitude, longitude)
        # if the user input has multiple state associated with the same city same
        elif len(create_list) > 1:
            print("City " + city_name.upper() + " is seen in " + str(len(create_list)) + " states")

            loop_city = 0
            while loop_city < 3:
                for n in range(len(create_list)):
                    text = colored(create_list[n], 'blue')
                    print("If you like to read the weather conditions in " + text + " " + "select :" + colored(
                        (str(n + 1)), 'blue'))

                # receive input from user, to identify the state where city is location
                # after three attempts, user is provided a different option

                input_message = int(input("Please select a choice of state:"))
                if 1 <= input_message <= len(create_list):
                    name = city_name_data[input_message - 1]['name']
                    latitude = city_name_data[input_message - 1]['lat']
                    longitude = city_name_data[input_message - 1]['lon']
                    get_weather(name, latitude, longitude)
                    break
                else:
                    if loop_city > 1:
                        print("You have entered an invalid option three time. Terminating program !!!!!!!!!!!!")
                        break
                    else:
                        print("You have selected an invalid option")
                loop_city = loop_city + 1
        else:
            print("Entered city {} not found or no information available".format(colored(city_name, 'blue')))


def main():
    loop_check = 0
    print("")
    # receive input from user, if they want to check the temperature by zipcode or city name
    # loop 3 times before terminating if the user did not enter option 1 (zipcode) or 2(City name)
    while loop_check < 3:
        loop_check = loop_check + 1
        print(colored("Select from the following available options:", "blue"))
        print("1 - Weather by Zipcode")
        print("2 - Weather by City")
        print("3 - Terminate the program")
        print(" ")
        input_option = input("Select your option:")
        print(" ")
        # if user selected zipcode, go to function get_zipcode
        if input_option == "1":
            get_zipcode()
        # if user selected zipcode, go to function get_city_name
        elif input_option == "2":
            get_city_name()
        # if user selected option 3, terminate the program
        elif input_option == "3":
            print("Thank you for visiting. Terminating program")
            break
        # if user selected an option other than 1, 2 or 3 , request the user to input the value again
        # after three attempts, user is provided a different option
        else:
            if loop_check == 2:
                print("You have entered an invalid option three times. Terminating program !!!!!!!!!!!!")
                break
            else:
                print("You have entered an invalid option: {}".format(colored(input_option, 'blue')))

        # receive input from user, if they want to continue to check temperature of another city
        # loop 3 times before terminating if the user did not enter Y or N
        loop_item = 0
        while loop_item < 3:
            print(" ")
            input_message = input("Do you like to check the weather for another city (Y/N) : ")
            print(" ")
            # if user selected "Y" continue to check other city temperature, continue the program
            if input_message.upper() == "Y":
                loop_check = 0
                break
            # if user selected "N" , exit the program
            elif input_message.upper() == "N":
                loop_check = 4
                print("")
                print("Thank you for using Reenie's weather channel. Good bye.")
                break
            # if user selected an option other than "Y" or "N" , request the user to input the value again
            # after three attempts, user is provided a different option
            else:
                print("You have entered an invalid option.")
                if loop_item == 2:
                    print("You had three incorrect attempts. Terminating the program!")
                    break


# using special variable
if __name__ == "__main__":
    print("Welcome to Reenie's weather Channel!!")
    main()
