# from colorama import init
# from termcolor import colored
# import emoji
import datetime
import random
import time

from art import *
from tqdm import tqdm

# Var for showing welcome text In ASCII Chars
art_1 = text2art("Welcome", font="rnd-medium")
# Documentation
docs = open("READ.md", "rt")
# parallel arrays
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular', 'Radiology', 'Rebhilitaion', 'neurology', 'Onocology Exams',
            'Physical Therapy', 'Plastic Surgery', 'Allergy Test']
prices = [75.0, 450.0, 11879.0, 384.4, 900.0]
# parallel arrays
services_used = []
prices_used = []

medicine = {"NALTREXONE": 120.23, "METHADONE": 44.39, "NARATRIPTAN": 60.00, "CHEMOTHERAPY": 10000.00,
            "DEXAMETHASONE": 16.00, 'EPINEPHRINE': 173.45, 'ABMIEN': 153.00, 'PENICILLIN': 35.84, }
line = "\n==================================================="


def custom_services(custom_selection):
    print("Enter your custom services and prices used: (type 'q' to when finished)")
    custom_selection = custom_selection.lower()
    if custom_selection == 'y':
        while custom_selection != 'q':
            custom_service = input("Enter the additional service used: ")
            if custom_service == 'q':
                break
            custom_price = input("Enter the price of the service: $")
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
    user_room_rate = float(input("Enter how many days in the hospital you spent "))
    days_price = (3109.0 * user_room_rate)
    return days_price


def medicine_choice(pay_choice):
    print("\n")
    print("Here is a list of medicine that we have! \n")

    for key in sorted(medicine):
        print(f"\t\t\t{key} -> {medicine[key]}\n")

    print(line)

    user_medicine_choice = " "

    medicine_prices = 0

    while user_medicine_choice != 'q':
        user_medicine_choice = str(input("What medicine were you perscribed? (type value >)"))
        for key, values in medicine:
            if user_medicine_choice.upper() in medicine.keys():
                medicine[key] = medicine_prices
                print(medicine[key])
                print(medicine_prices)
                break
            break
            # elif user_medicine_choice == 'q':
            #   break
            # else:
            #   print("Not a valid answer")
            #    continue

    # total_medicine_price = sum(used_medicine.values())

    # if pay_choice == 'n':
    #     total_medicine_price *= 0.25
    # return total_medicine_price


# if (user_medicine_choice != medicine):
# print("Medicine does not exist")
# elif (user_medicine_choice == medicine(p)):

# elif (user_medicine_choice == 'q'):
# break


def service_choice(insurance_discount, pay_choice):
    final_choice = 0.0
    final_choice = float(final_choice)

    multi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

    print("\n=========== Enter the Services Used ============\n")
    for (i, j) in zip(services, multi):
        print(f"\t\t\t\t{j.upper()}.\t\t{i.upper()}\t\t\t\t\n")

    print(line)

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
    return final_choice


def final_statement(today, days_price):
    nurse_first_name = ["bob", "sally", "joel", "henry", "lucy"]
    nurse_last_name = ["smith", "rodriguez", "jefferson", "chin"]

    random_FN = random.choice(nurse_first_name)
    random_LN = random.choice(nurse_last_name)

    print("\nCalculating bill... ")

    for _ in tqdm(range(100)):
        time.sleep(.02)

    print("\n")
    print("\t\t\t\t++++++++This is your final bill++++++++")
    print(f"{today: %B %d, %Y}\t\t\t\t\tNurse: {random_FN}, {random_LN}")

    sum_total = final_choice * days_price

    print(f"this is the sum {sum_total}")


def inpatient():
    today = datetime.datetime.today()

    while True:
        pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            custom_services(input("Did you have any additional services? (type y or n) "))
            room_rate()
            medicine_choice('y')
            final_statement(today, 1095.0)
            break
        elif pay_choice.lower() == 'n':
            print("This means that your insurance will cover most you will pay 25% of final cost")
            service_choice(0.25, 'n')
            custom_services(custom_selection=str(input("Did you have any additional services? (type y or n) ")))
            room_rate()
            medicine_choice('n')
            final_statement(today, 1095.0)
            break
        else:
            print("Not a valid input")
            pass


def outpatient():
    pass


# This is the where the user inputs a choice
def greeting(user_1, user_2, time_now):
    print("Welcome to a hospital project for _____ children hospital\nEnter 'd' to refer to documentation before going "
          "further! Enjoy\n")
    print(f"Written by {user_1} and {user_2} {time_now}\n\n")


def main():
    print(art_1)
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
