# from colorama import init
# from termcolor import colored
# import emoji
import time
from tqdm import tqdm
from art import *
import urllib
import datetime

art_1 = text2art("Welcome", font="rnd-medium")
print(art_1)

# Documentation
docs = open("READ.md", "r")
# parell arrays
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular']
prices = [350, 403, 323, 384]
# parell arrays
services_used = []
prices_used = []

medicine = []
multi = ['a', 'b', 'c', 'd']


def custom_services(custom_selection):
    print("\n")
    print("Enter your custom services and prices used: (type 'q' to when finished)")
    custom_selection = custom_selection.lower()
    if custom_selection == 'y':
        while custom_selection != 'q':
            custom_service = str(input("Enter the additional service used: "))
            if custom_service == 'q':
                services_used.append(custom_service)
                break
            custom_price = int(input("Enter the price of the service: $"))
            if custom_price == 'q':
                prices_used.append(custom_price)
                break

    elif custom_selection == 'n':
        pass
    else:
        print("Not a valid input")
        custom_services(custom_selection)
    print("Thanks for your input! Here are all the services used")
    # services_used.append(custom_service)
    #  prices_used.append(custom_price)

    print(f"--- services used---")
    for (i, j) in zip(services_used, prices_used):
        print(f"{i} and the price is ${j}")


def room_rate():
    input("Enter how many days in the hospital you spent ")


def medicine_choice():
    print("something")


def service_choice():
    user_choice_multi = " "
    final_choice = 0
    print("\n")
    print("************ Enter the service that used ************\n")

    for (i, j) in zip(services, multi):
        print("\t\t\t----------------------\n")
        print(f"\t\t\t      {j} {i}      \n")

    while user_choice_multi.lower() != 'q':
        user_choice_multi = str(input("Enter Service Used (type 'q' when finished): "))
        user_choice_multi = user_choice_multi.lower()
        if user_choice_multi.lower() == multi[0]:
            services_used.append(services[0])
            prices_used.append(prices[0])
            final_choice += prices[0]
        elif user_choice_multi.lower() == multi[1]:
            services_used.append(services[1])
            prices_used.append(prices[1])
            final_choice += prices[1]
        elif user_choice_multi.lower() == multi[2]:
            services_used.append(services[2])
            prices_used.append(prices[2])
            final_choice += prices[2]
        elif user_choice_multi.lower() == multi[3]:
            services_used.append(services[3])
            prices_used.append(prices[3])
            final_choice += prices[3]
        elif user_choice_multi.lower() == 'q':  # WIP update so user will not crash program with invalid value -matt
            print("Thank you for your selection")
            break
        print(final_choice)

    print(final_choice)

    # outputs correctly make it easier to read WIP
    # sum = final_choice * 450
    # print(f"this is the sum {sum}")


def final_statement(today):
    print("Calculating bill... ")
    for _ in tqdm(range(100)):
        time.sleep(.04)
    print("\n")
    print("++++++++This is your final bill++++++++")
    print(f"{today: %B %d, %Y}")


def inpatient():
    # Date for final bill
    today = datetime.datetime.today()
    while True:
        pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice()
            # Additional Service should account for null answers
            custom_services(custom_selection=str(input("Did you have any additional services? (type y or n) ")))
            room_rate()
            medicine_choice()
            final_statement(today)
            break
        elif pay_choice == 'n':
            service_choice()
            break
        else:
            print("Not a valid input")
            pass

    # days = int(input("Number of days in the hospital: "))
    print("This is your room rate $ ")


def outpatient():
    print("outpatient")


# This is the where the user inputs a choice
def main():
    time_now = datetime.date(2022, 11, 23)
    userChoice = input("Enter i for Inpatient o for Outpatient: ")
    userChoice = userChoice.lower()
    if userChoice == "i":
        inpatient()
    elif userChoice == "o":
        outpatient()
    else:
        print("Not a correct choice\rPlease refer to documentation ")
        docs.read()
        # print(emoji.emojize(":grinning_face_with_big_eyes:"))
        main()

    print(f"Written by Matt and Kevin {time_now}")


if __name__ == "__main__":
    try:
        main()
    except EnvironmentError:
        print("Not a valid program")
