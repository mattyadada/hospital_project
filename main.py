# Matt McCarthy & Kevin Alves 12/6/22 COP1000-1
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
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular', 'Radiology', 'Rehabilitation', 'neurology', 'Oncology Exams',
            'Physical Therapy', 'Plastic Surgery', 'Allergy Test']
prices = [75.0, 450.0, 11879.0, 384.4, 900.0, 9000.0, 10000.9, 140.0, 2030.40, 714.32, 24.50]
# parallel arrays
services_used = []
service_prices_used = []

medicine_list = ["NSAID", "HYDROCODONE", "NARATRIPTAN", "CHEMOTHERAPY",
                 "DEXAMETHASONE", 'EPINEPHRINE', 'AMBIEN', 'PENICILLIN']
medicine_prices = [120.21, 44.39, 60.00, 10000.00, 16.00, 173.45, 153.00, 35.84]

medicine_prices_used = []
line = "\n==================================================="


def custom_services(custom_selection, pay_choice):
    print("Enter your custom services and prices used")
    custom_selection = custom_selection.lower()
    if custom_selection == 'y':
        custom_service = " " 
        custom_price = 0.0
        while custom_selection != 'q' or custom_service.lower() != 'q' or custom_price.lower() != 'q':
            custom_service = input("Enter the additional service used (type 'q' on service when done): ")
            if custom_service == 'q' or custom_service == 'Q':
                break
            services_used.append(custom_service)
		
            custom_price = float(input("Enter the cost of the service: $"))
            if pay_choice == 'y':
                service_prices_used.append(float(custom_price))
            else:
                service_prices_used.append(float(custom_price * .25))
    elif custom_selection == 'n':
        pass
    elif custom_selection != 'n' or custom_selection != 'y':
        custom_services('y', pay_choice)

    print(f"---services used---")
    for (i, j) in zip(services_used, service_prices_used):
        print(f"{i} and the price is ${j}")


def medicine_choice(insurance_discount, pay_choice):
    # change it so
    # work on a nested for loop  to get first 2 values of each string and append corresponding prices to new array
    print("\n")
    print("========= Medications in stock ===========\n")
    for (i, j) in zip(medicine_list, medicine_prices):
        print(f"\t\t\t{i} -> {j}\t\t\t\t\n")
    print(line)

    user_medicine_choice = " "

    print("\nEnter the medication the patient was prescribed? (type Abbreviated value (ex. AMB for AMBIEN): ")

    if pay_choice == 'y':
        while user_medicine_choice != 'q':
            user_medicine_choice = str(input("Enter medication (type 'q' when finished) :  "))
            if user_medicine_choice.upper() == "NSA":
                medicine_prices_used.append(medicine_prices[0])
            elif user_medicine_choice.upper() == "HYD":
                medicine_prices_used.append(medicine_prices[1])
            elif user_medicine_choice.upper() == "NAP":
                medicine_prices_used.append(medicine_prices[2])
            elif user_medicine_choice.upper() == "CHE":
                medicine_prices_used.append(medicine_prices[3])
            elif user_medicine_choice.upper() == "DEX":
                medicine_prices_used.append(medicine_prices[4])
            elif user_medicine_choice.upper() == "EPI":
                medicine_prices_used.append(medicine_prices[5])
            elif user_medicine_choice.upper() == "AMB":
                medicine_prices_used.append(medicine_prices[6])
            elif user_medicine_choice.upper() == "PEN":
                medicine_prices_used.append(medicine_prices[7])
            elif user_medicine_choice != 'q' or user_medicine_choice != 'Q':
                continue
    if pay_choice == 'n':
        while user_medicine_choice != 'q':
            user_medicine_choice = str(input("Enter medication (type 'q' when finished) :  "))
            if user_medicine_choice.upper() == "NAL":
                medicine_prices_used.append(medicine_prices[0] * insurance_discount)
            elif user_medicine_choice.upper() == "MET":
                medicine_prices_used.append(medicine_prices[1] * insurance_discount)
            elif user_medicine_choice.upper() == "NAP":
                medicine_prices_used.append(medicine_prices[2] * insurance_discount)
            elif user_medicine_choice.upper() == "CHE":
                medicine_prices_used.append(medicine_prices[3] * insurance_discount)
            elif user_medicine_choice.upper() == "DEX":
                medicine_prices_used.append(medicine_prices[4] * insurance_discount)
            elif user_medicine_choice.upper() == "EPI":
                medicine_prices_used.append(medicine_prices[5] * insurance_discount)
            elif user_medicine_choice.upper() == "AMB":
                medicine_prices_used.append(medicine_prices[6] * insurance_discount)
            elif user_medicine_choice.upper() == "PEN":
                medicine_prices_used.append(medicine_prices[7] * insurance_discount)
            elif user_medicine_choice != 'q' or user_medicine_choice != 'Q':
                continue


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
            service_prices_used.append(prices[0])
        elif user_choice_services.lower() == multi[1]:
            services_used.append(services[1])
            service_prices_used.append(prices[1])
        elif user_choice_services.lower() == multi[2]:
            services_used.append(services[2])
            service_prices_used.append(prices[2])
        elif user_choice_services.lower() == multi[3]:
            services_used.append(services[3])
            service_prices_used.append(prices[3])
        elif user_choice_services.lower() == multi[4]:
            services_used.append(services[4])
            service_prices_used.append(prices[4])
        elif user_choice_services.lower() == multi[5]:
            services_used.append(services[5])
            service_prices_used.append(prices[5])
        elif user_choice_services.lower() == multi[6]:
            services_used.append(services[6])
            service_prices_used.append(prices[6])
        elif user_choice_services.lower() == multi[7]:
            services_used.append(services[7])
            service_prices_used.append(prices[7])
        elif user_choice_services.lower() == multi[8]:
            services_used.append(services[8])
            service_prices_used.append(prices[8])
        elif user_choice_services.lower() == multi[9]:
            services_used.append(services[9])
            service_prices_used.append(prices[9])
        elif user_choice_services.lower() == multi[10]:
            services_used.append(services[10])
            service_prices_used.append(prices[10])
        # Add necessary multis and services/ prices
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
            service_prices_used.append(prices[0] * insurance_discount)
        elif user_choice_services.lower() == multi[1]:
            services_used.append(services[1])
            service_prices_used.append(prices[1] * insurance_discount)
        elif user_choice_services.lower() == multi[2]:
            services_used.append(services[2])
            service_prices_used.append(prices[2] * insurance_discount)
        elif user_choice_services.lower() == multi[3]:
            services_used.append(services[3])
            service_prices_used.append(prices[3] * insurance_discount)
        elif user_choice_services.lower() == multi[4]:
            services_used.append(services[4])
            service_prices_used.append(prices[4] * insurance_discount)
        elif user_choice_services.lower() == multi[5]:
            services_used.append(services[5])
            service_prices_used.append(prices[5] * insurance_discount)
        elif user_choice_services.lower() == multi[6]:
            services_used.append(services[6])
            service_prices_used.append(prices[6] * insurance_discount)
        elif user_choice_services.lower() == multi[7]:
            services_used.append(services[7])
            service_prices_used.append(prices[7] * insurance_discount)
        elif user_choice_services.lower() == multi[8]:
            services_used.append(services[8])
            service_prices_used.append(prices[8] * insurance_discount)
        elif user_choice_services.lower() == multi[9]:
            services_used.append(services[9])
            service_prices_used.append(prices[9] * insurance_discount)
        elif user_choice_services.lower() == multi[10]:
            services_used.append(services[10])
            service_prices_used.append(prices[10] * insurance_discount)
        # Add necessary multis and services/ prices
        elif user_choice_services.lower() == 'q':  # WIP update so user will not crash program with invalid value -matt
            print("Thank you for your selection")
            break
        else:
            print("Not a valid input try again!")
            continue


def final_statement(today, days_price, patient_status, user_days):
    nurse_first_name = ["Bob", "Sally", "Joel", "Henry", "Lucy"]
    nurse_last_name = ["Smith", "Rodriguez", "Jefferson", "Chin"]

    random_FN = random.choice(nurse_first_name)
    random_LN = random.choice(nurse_last_name)

    print("\nCalculating bill... ")

    for _ in tqdm(range(100)):
        time.sleep(.02)

    print("\t\t\t++++++++This is your final bill++++++++")
    print("\n")
    print(f"{today: %B %d, %Y}\t\t\t\t\tNurse: {random_FN}, {random_LN}")

    # services_prices_sum = 0
    # medicine_prices_sum = 0

    room_charges = days_price * user_days

    services_prices_sum = sum(service_prices_used)
    medicine_prices_sum = sum(medicine_prices_used)

    sum_total_inpatient = services_prices_sum + room_charges + medicine_prices_sum
    sum_total_outpatient = services_prices_sum + medicine_prices_sum

    print('\n')
    print(line)
    print('\n')

    if patient_status.lower() == "i":
        print(f"Room charges    $ {room_charges}")
        print(f"Labs & Services $ {services_prices_sum}")
        print(f"Medication      $ {medicine_prices_sum}")
        print(f"Total charges   $ {sum_total_inpatient}")
    else:
        print(f"Labs & Services $ {services_prices_sum}")
        print(f"Medication      $ {medicine_prices_sum}")
        print(f"Total charges   $ {sum_total_outpatient}")

    print('\n')
    print(line)
    print('\n')


def inpatient():
    today = datetime.datetime.today()

    while True:
        pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            custom_services(input("Did you have any additional services? (type y or n) "), 'y')
            medicine_choice(0.25, 'y')
            final_statement(today, 1095.0, "i", user_days=float(input("Enter how days did you spent in the hospital? ")))
            break
        elif pay_choice.lower() == 'n':
            print("This means that your insurance will cover most you will pay 25% of final cost")
            service_choice(0.25, 'n')
            custom_services(input("Did you have any additional services? (type y or n) "), 'n')
            medicine_choice(0.25, 'n')
            final_statement(today, 1095.0, "o", user_days=float(input("Enter how many days did you spent in the hosptial? ")))
            break
        else:
            print("Not a valid input")
            pass
    return pay_choice


def outpatient():
    today = datetime.datetime.today()

    while True:
        pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            custom_services(input("Did you have any additional services? (type y or n) "), 'y')
            medicine_choice(0.25, 'y')
            final_statement(today, 1095.0, "i" )
            break
        elif pay_choice.lower() == 'n':
            print("This means that your insurance will cover most you will pay 25% of final cost")
            service_choice(0.25, 'n')
            custom_services(input("Did you have any additional services? (type y or n) "), 'n')
            medicine_choice(0.25, 'n')
            final_statement(today, 1095.0, "o",)
            break
        else:
            print("Not a valid input")
            pass
    return pay_choice


# This is the where the user inputs a choice
def greeting(user_1_firstname, user_1_lastname, user_2_firstname, user_2_lastname, time_now):
    print("Welcome to a hospital project for _____ children hospital\nEnter 'd' to refer to documentation before going "
          "further! Enjoy\n")
    print(f"Written by {user_1_firstname} {user_1_lastname} and {user_2_firstname} {user_2_lastname} {time_now}\n\n")


def main():
    print(art_1)
    greeting("Matt", "McCarthy", "Kevin", "Alves", datetime.date(2022, 11, 23))

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
