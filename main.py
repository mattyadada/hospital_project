# from colorama import init
# from termcolor import colored
# import emoji
import random
import time
from tqdm import tqdm
from art import *
import urllib
import datetime

art_1 = text2art("Welcome", font="rnd-medium")
print(art_1)

# Documentation
docs = open("READ.md", "rt")
# parallel arrays
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular']
prices = [350.0, 403.2, 323.3, 384.4]
# parallel arrays
services_used = []
prices_used = []

medicine = []


def custom_services(custom_selection):
    print("\n")
    print("Enter your custom services and prices used: (type 'q' to when finished)")
    custom_selection = custom_selection.lower()
    if custom_selection == 'y':
        while custom_selection != 'q':
            custom_service = str(input("Enter the additional service used: "))
            if custom_service == 'q':
                break
            custom_price = int(input("Enter the price of the service: $"))
            if custom_price == 'q':
                prices_used.append(custom_price)
                break
            prices_used.append(custom_price)
            services_used.append(custom_service)

    elif custom_selection == 'n':
        pass
    else:
        print("Not a valid input")
        custom_services(custom_selection)
    print("Thanks for your input! Here are all the services used")

    print(f"--- services used---")
    for (i, j) in zip(services_used, prices_used):
        print(f"{i} and the price is ${j}")


def room_rate():
    user_room_rate = input("Enter how many days in the hospital you spent ")
    return user_room_rate


def medicine_choice():
    print("something")


def service_choice(insurance_discount, pay_choice):
    final_choice = 0.0
    multi = ['a', 'b', 'c', 'd']
    print("\n")
    print("************ Enter the service that used ************\n")

    for (i, j) in zip(services, multi):
        print("\t\t\t----------------------\n")
        print(f"\t\t\t      {j} {i}      \n")

    while pay_choice == 'y':
        user_choice_services = str(input("Enter Service Used (type 'q' when finished): "))
        user_choice_services = user_choice_services.lower()
        if user_choice_services.lower() == multi[0]:
            services_used.append(services[0])
            prices_used.append(prices[0])
            final_choice += prices[0]
        elif user_choice_services.lower() == multi[1]:
            services_used.append(services[1])
            prices_used.append(prices[1])
            final_choice += prices[1]
        elif user_choice_services.lower() == multi[2]:
            services_used.append(services[2])
            prices_used.append(prices[2])
            final_choice += prices[2]
        elif user_choice_services.lower() == multi[3]:
            services_used.append(services[3])
            prices_used.append(prices[3])
            final_choice += prices[3]
        elif user_choice_services.lower() == 'q':  # WIP update so user will not crash program with invalid value -matt
            print("Thank you for your selection")
            break
        else:
            print("Not a valid choice")
            continue
        print(final_choice)
    print(final_choice)

    while pay_choice.lower() == 'n':
        user_choice_services = str(input("Enter Service Used (type 'q' when finished): "))
        user_choice_services = user_choice_services.lower()
        if user_choice_services.lower() == multi[0]:
            services_used.append(services[0])
            prices_used.append(prices[0])
            final_choice += prices[0] * insurance_discount
        elif user_choice_services.lower() == multi[1]:
            services_used.append(services[1])
            prices_used.append(prices[1])
            final_choice += prices[1] * insurance_discount
        elif user_choice_services.lower() == multi[2]:
            services_used.append(services[2])
            prices_used.append(prices[2])
            final_choice += prices[2] * insurance_discount
        elif user_choice_services.lower() == multi[3]:
            services_used.append(services[3])
            prices_used.append(prices[3])
            final_choice += prices[3] * insurance_discount
        elif user_choice_services.lower() == 'q':  # WIP update so user will not crash program with invalid value -matt
            print("Thank you for your selection")
            break
        else:
            print("Not a valid input try again!")
            continue
        print(final_choice)
    print(final_choice)

    # outputs correctly make it easier to read WIP
    days = float(input("enter days"))
    days_price = 450.0 * days
    sum_total = final_choice * days_price
    print(f"this is the sum {sum_total}")


def final_statement(today):
    nurse_first_name = ["bob", "sally", "joel", "henry", "lucy"]
    nurse_last_name = ["smith", "rodriguez", "jefferson", "chin"]
    random_FN = random.choice(nurse_first_name)
    random_LN = random.choice(nurse_last_name)
    print("\nCalculating bill... ")
    for _ in tqdm(range(100)):
        time.sleep(.04)
    print("\n")
    print("\t\t\t\t++++++++This is your final bill++++++++")
    print(f"{today: %B %d, %Y}\t\t\t\t\tNurse: {random_FN}, {random_LN}")


def inpatient():
    today = datetime.datetime.today()
    while True:
        pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            # Additional Service should account for null answers
            custom_services(custom_selection=str(input("Did you have any additional services? (type y or n) ")))
            room_rate()
            medicine_choice()
            final_statement(today)
            break
        elif pay_choice.lower() == 'n':
            print("This means that your insurance will cover most you will pay 25% of final cost")
            service_choice(0.25, 'n')
            custom_services(custom_selection=str(input("Did you have any additional services? (type y or n) ")))
            room_rate()
            medicine_choice()
            final_statement(today)
            break
        else:
            print("Not a valid input")
            pass


def outpatient():
    print("outpatient")


# This is the where the user inputs a choice
def greeting(user_1, user_2, time_now):
    print("Welcome to a hospital project for _____ children hospital\nEnter 'd' to refer to documentation before going "
          "further! Enjoy\n")
    print(f"Written by {user_1} and {user_2} {time_now}\n\n")


def main():
    greeting("Matt", "Kevin", datetime.date(2022, 11, 23))
    userChoice = input("Enter i for Inpatient o for Outpatient: ")
    userChoice = userChoice.lower()
    if userChoice == "i":
        inpatient()
    elif userChoice == "o":
        outpatient()
    elif userChoice == "d":
        print(docs.read())
        main()
    else:
        print("Not a correct choice\rPlease refer to documentation ")
        # print(emoji.emojize(":grinning_face_with_big_eyes:"))
        main()


if __name__ == "__main__":
    try:
        main()
    except EnvironmentError:
        print("Not a valid program")
