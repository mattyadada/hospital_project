from colorama import init
from termcolor import colored
from art import *
import datetime


# x = datetime.datetime.now()
# print(x)

art_1 = text2art("Welcome", font="rnd-medium")
print(art_1)

# services and prices are paralell arrays
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular']
multi = ['a', 'b', 'c', 'd']
prices = [350, 403, 323, 384]
# medicine is its own array
medicine = []


def multi_choice():
    print("************ Enter the services that used ************\n")

    for (i, j) in zip(services, multi):
        print("For " + i + '\tEnter ' + j)

    while True:
        user_choice_multi = str(input("Enter Service Used: "))
        if user_choice_multi.lower() == multi[0]:
            final_choice = prices[0]
            break
        elif user_choice_multi.lower() == multi[1]:
            final_choice = prices[1]
            break
        elif user_choice_multi.lower() == multi[2]:
            final_choice = prices[2]
            break
        elif user_choice_multi.lower() == multi[3]:
            final_choice = prices[3]
            break
        else:  # WIP update so user will not crash program with invalid value -matt
            print('You did not type in a valid statement')
            pass

    # outputs correctly make it easier to read WIP
    sum = final_choice * 450
    print("this is the sum ${p}".format(p=sum))


def inpatient():
    payChoice = str(input("Are you self payed? Enter y or n: "))
    if payChoice.lower() == 'y':
        multi_choice()
    elif payChoice == 'n':
        print("These are your choices")
    # days = int(input("Number of days in the hospital: "))
    charges = int(input("Enter daily room rate: "))
    print("This is your room rate $ ")


def outpatient():
    print("outpatient")


# This is the where the user inputs a choice
userChoice = input("Enter i for Inpatient o for Outptient: ")
if userChoice.lower() == "i":
    inpatient()
elif userChoice == "o":
    outpatient()


def error():
    print("Not a valid input")

