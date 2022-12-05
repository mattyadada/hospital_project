# Welcome To a Hospital Project 
#### This is Project is based on [Joe DiMaggio Children's Hospital](https://www.jdch.com/) (No affiliation)
#### Written by Matt McCarthy and Kevin Alves 12/6/2022
#### COP1000-1
### Professor: Dr. Kharis Kerby Sibayan

### Introduction
This program is based on a hospital billing system. It is meant to showcase 
work learned throughout COP-1000 at PBSC. We intend to showcase our developing programming skills developed such as
1. How to use
2. Arrays
   1. Parallel Arrays
3. Variables Datatypes
4. If/Else conditional statements
5. For Loops
6. While loops
7. Functions
8. Extras

### Installation 
Make sure python is installed with `python --version`
Begin by cloning the `git` repository 

```
git clone https://github.com/mattyadada/hospital_project.git 
```
`cd` Into directory. 
Then run from terminal run `python main.py` or `python3 main.py`

# 1. How to use 
In this program, you will be able to access the Joe DiMaggio Children's Hospital's user interface to determine the exact cost of services, labs, medicine, room rates (per night) and other fees as an inpatient or outpatient at the hospital.
### Step 1.
 The code will ask if you are an inpateint or oupaitent (This will determine whether or not you stayed at the hospital overnight). You can choose by entering the letters I or O in both lowercase and uppercase format.
```  
 userChoice = input("Enter i for Inpatient o for Outpatient: ")
    userChoice = userChoice.lower()
```
### Step 2.
 Once you've determined which patient you are, the code will ask if you are self-paying, to which you can respond Y or N. The code will then tell you whether or not your insurance will cover the cost of your visit. The code will then direct you to enter the type of services you've received by inputting letters a through k. (If you are  finished inputing your serivces enter q). Furthermore, depending on whether you choose inpatient or outpatient care, you will be asked how many days you spent in the hospital overnight.
``` 
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular', 'Radiology', 'Rebhilitaion', 'neurology', 'Onocology Exams', 'Physical Therapy', 'Plastic Surgery', 'Allergy Test']
```
### Step 3.
  After adding you the services provided the code will then ask for additinonal serivices inputed and the prices of those services. You can add any number of services as needed and to finish entering your services just enter to q to finsih. The program will then output the cost of each service selected and the name and price of each service inputed.
```
print("Enter your custom services and prices used: (type 'q' to when finished)")
    custom_selection = custom_selection.lower()
    if custom_selection == 'y':
        while custom_selection != 'q':
            custom_service = input("Enter the additional service used: ")
            if custom_service == 'q':
                break
            custom_price = float(input("Enter the price of the service: $"))
            if custom_price == 'q':
                break
            services_used.append(custom_service)
            service_prices_used.append(custom_price)

    elif custom_selection == 'n':
        pass
    elif custom_selection != 'n' or custom_selection != 'y':
        print("Not a valid input")
        custom_services(custom_selection)
    print("Thanks for your input! Here are all the services used")

    print(f"--- services used---")
    for (i, j) in zip(services_used, service_prices_used):
        print(f"{i} and the price is ${j}")
```
### Step 4.
 After entering all of the service information, you are asked which medicine you were prescribed in relation to the services provided. The code will direct you to enter the medication's name or an abbrivated verison of the word (ex. AMB for AMBIEN). The medication's name and price will be displayed above. To finish, enter your chosen medication and press q.
```
 print("\nEnter the medication the patient was prescribed? (type Abbreviated value (ex. AMB for AMBIEN): ")

    if pay_choice == 'y':
        while user_medicine_choice != 'q':
            user_medicine_choice = str(input("Enter medication (type 'q' when finished) :  "))
            if user_medicine_choice.upper() == "NAL":
                medicine_prices_used.append(medicine_prices[0])
            elif user_medicine_choice.upper() == "MET":
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
```
### Step 5.
 Now that all of the code has been inputed the program will load all of your information. The code will display the prices of all of your services, medication, roomrate and how many nights you spent, and how much your insurance your covered.
```
def final_statement(today, days_price, patient_status):
    nurse_first_name = ["Bob", "Sally", "Joel", "Henry", "Lucy"]
    nurse_last_name = ["Smith", "Rodriguez", "Jefferson", "Chin"]

    random_FN = random.choice(nurse_first_name)
    random_LN = random.choice(nurse_last_name)

    print("\nCalculating bill... ")

    for _ in tqdm(range(100)):
        time.sleep(.02)

    print("\n")
    print("\t\t\t++++++++This is your final bill++++++++")
    print(f"{today: %B %d, %Y}\t\t\t\t\tNurse: {random_FN}, {random_LN}")

    # services_prices_sum = 0
    # medicine_prices_sum = 0

    services_prices_sum = sum(service_prices_used)
    medicine_prices_sum = sum(medicine_prices_used)
    # for _ in service_prices_used:
    #     services_prices_sum += 1
    # for _ in medicine_prices_used:
    #     medicine_prices_sum += 1

    sum_total_inpatient = services_prices_sum * days_price * medicine_prices_sum
    sum_total_outpatient = services_prices_sum * medicine_prices_sum

    print('\n')
    print(line)
    print('\n')

    if patient_status.lower() == "i":
        print(f"Room charges    $ {days_price}")
        print(f"Labs & Services $ {services_prices_sum}")
        print(f"Medication      $ {medicine_prices_sum}")
        print(f"Total charges   $ {sum_total_inpatient}")
    else:
        print(f"this is the sum {sum_total}")
        print(f"Labs & Services $ {services_prices_sum}")
        print(f"Medication      $ {medicine_prices_sum}")
        print(f"Total charges   $ {sum_total_outpatient}")

    print('\n')
    print(line)
    print('\n')
```
# 2.Arrays
###  Parallel Arrays
The code includes two parallel arrays, the first of which contains the arrays for service and service fees. The "services array" is a string containing the names of the services provided by the program. The "prices array" contains fixed price values for each service provided by the hospital.
```
services = ['Xrays', 'CT Scan', 'Surgery', 'Vascular', 'Radiology', 'Rehabilitation', 'neurology', 'Oncology Exams',
            'Physical Therapy', 'Plastic Surgery', 'Allergy Test']
prices = [75.0, 450.0, 11879.0, 384.4, 900.0]
```
The second set of parallel arrays has a similar output to the previous array, this time for a list of medication distribution prices for the services provided. The "medicine list array" is a string of medicine names that the user can see in order to help them decide which medicine to use. For the "medicine prices array," which is similar to the "medicine list array," they will display together with the array's name and price.
```
medicine_list = ["NALTREXONE", "METHADONE", "NARATRIPTAN", "CHEMOTHERAPY",
                 "DEXAMETHASONE", 'EPINEPHRINE', 'AMBIEN', 'PENICILLIN']
medicine_prices = [120.21, 44.39, 60.00, 10000.00, 16.00, 173.45, 153.00, 35.84]

medicine_prices_used = []
```
# 3. Variables Datatypes
The variables that stand out the most in the program are "final_statement" and "pay_choice" Both of these variations are largely what distinguishes this program from others.
### final_statement
The variable "final_statement" contributes greatly to code because it contains all of the information collected from the user inputs. The "final statement" will list all of the services, costs, medications, room costs, days spent in the hospital, and the overall cost of the patient's stay.  This gives the program a distinct look near the end.
```
final_statement(today, days_price, patient_status, user_days)
```
"pay choice" adds significant value to the code by requesting whether the user intends to self-pay or not. If you enter y for yes, the program will add a new value of 25% of insurance assistance. If no is entered, the code will calculate the program without including the 25% of insurance assistance in the total output.
```
 pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            custom_services(input("Did you have any additional services? (type y or n) "))
            medicine_choice(0.25, 'y')
            final_statement(today, 1095.0, "i" )
            break
        elif pay_choice.lower() == 'n':
            print("This means that your insurance will cover most you will pay 25% of final cost")
            service_choice(0.25, 'n')
```
# 5. If/else statements
With so many options to choose from in a program, it's only natural to use if/else statements within the code. The following two if/else statements stand out the most: "if pay choice.lower(), if user medicine choice.upper()." Both of these statements allow the code to provide the user with multiple options.

## "if pay choice.lower()"
This if/else statement asks questions whether you are self-payed or not. The statement will allow you to enter your answer in either lowercase or uppercase and will produce different results depending on your choice. If the user answered "y," the code will output code with the insurance rate, and if the user answered "n," the code will output code without the insurance rate, letting the user know, but both if/else statements will still print out  the same questions.
```
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
```
## if user medicine choice.upper()
The if/else "if user medicine choice.upper()" condition allows the user to select which medicine they want to take while in the hospital. The user has the option of entering any amount of medicine that is displayed. The if/else statement utilizes appened to extract a string or medicine names from the "medicine list" array. The code will also abbreviate the name of the medicine, so "CHEMOTHERAPY" could be entered as "che" or "CHE". If the user selects self payed, the if else statement also multiplies the price of the medicine by the insurance rate, and the price of the medicine is taken from the "medicine prices" array.
```
user_medicine_choice.upper() == "CHE":
                medicine_prices_used.append(medicine_prices[3])

medicine_list = ["NSAID", "HYDROCODONE", "NARATRIPTAN", "CHEMOTHERAPY",
                 "DEXAMETHASONE", 'EPINEPHRINE', 'AMBIEN', 'PENICILLIN']

medicine_prices = [120.21, 44.39, 60.00, 10000.00, 16.00, 173.45, 153.00, 35.84]
```

# 5. For Loops
For loops are primarily used in this program to output data from set arrays in the code. The for loops that output the user's information are printed out differently from one another to create a set for a more refined looking code. Also, keeping the user updated up until the final output.

In the code on lines 53 and 62 both codes output similar results. Both for loops take both inputs of the user and the parallel corralting to user input to display the output for the user. Each of the for loops display the type of serivce or medications along with prices.
```
Line 53
for (i, j) in zip(services_used, service_prices_used):
        print(f"{i} and the price is ${j}")
Line 62
 for (i, j) in zip(medicine_list, medicine_prices):
        print(f"\t\t\t{i} -> {j}\t\t\t\t\n")
    print(line)
```
An loop for loading bar was a unique for loop that was added to code to give it a unique look. This loop generates a loading bar that ranges from 0 to 100 to indicate that the program is loading data, with 100% indicating that all of the data is ready to be displayed. The for loop also ensures that each time the code is executed, a new nurse's name is displayed from an array within the code.
 ```
  for _ in tqdm(range(100)):
        time.sleep(.02)

    print("\t\t\t++++++++This is your final bill++++++++")
    print("\n")
    print(f"{today: %B %d, %Y}\t\t\t\t\tNurse: {random_FN}, {random_LN}")
```
# 6. While Loops
 While loops are primarily used in two ways in this program. The first is to receive input on the user services, and the second is to ask a yes or no question to generate a series of questions based on the user's responses. Both while loops contain a "if else" statement, with one of them depending on whether the user selects an in or out parameter.

 When the program first starts, one of the first questions it will ask is whether the user is an in or outpatient, as well as whether they are self-paying or not. If the user enters "Yes" for self-pay in the while loop's "if" statement, the program will inform you that you are not insured for your visit, and the "else" statement will request additional services while you are in the hospital. If the user enters "No" for self-pay, the loop will also output that the user is insured and will give them the percentage of coverage.
 ```
 while True:
        pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            custom_services(input("Did you have any additional services? (type y or n) "))
            medicine_choice(0.25, 'y')
            final_statement(today, 1095.0, "i" )
            break
        elif pay_choice.lower() == 'n':
            print("This means that your insurance will cover most you will pay 25% of final cost")
            service_choice(0.25, 'n')
            custom_services(custom_selection=str(input("Did you have any additional 
```
Another while loop takes the services that the user entered and multiplies them by the insurance percentage or not, depending on whether they are self-paying or not. The while loop will continue to prompt the user to enter any services used during their stay. The data is then stored in an array, and when the user is finished, they can simply enter "Q" to end the loop.
```
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
  ```
  # 7. Functions
 There are at least three main functions used in the making of this program to make it run more smoothly. "def main():, def inpatient(): def outpatient(): (smilliar to eachother), and " are the three functions. All three of these functions guide the program through the various choices a user will make in a systematic manner.

 ### def main(): Function
 The def main(): function begins the program by printing "Enter I for Inpatient o for Outpatient: " After this  output, we give the user some control by including "userChoice = userChoice.lower()" to give them the option of a lower or uppercase "o" or "i." If the user does not enter the answer correctly, the code will print " print("Not a correct choicerPlease refer to documentation ")" and they will be able to open a file of this documentation to learn more about the code.
 ```
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
```
### def inpatient(): and def outpatient(): Functions
  Both def inpatient(): and def outpatient(): are valid. Functions include paychoice, which calculates your insurance percentage based on "y" or "n," additional services, and the type of medication you were prescribed. The main difference between the two is that if you choose outpaient, the float input "Enter how many days did you spend in the hospital?" will be removed. That is, when the final statement is generated, the user will have saved more money because the program will not need to calculate the other fees with days stayed at the hospital.
```
  pay_choice = str(input("Are you self payed? Enter y or n: "))
        if pay_choice.lower() == 'y':
            service_choice(0.25, 'y')
            custom_services(input("Did you have any additional services? (type y or n) "), 'y')

user_days=float(input("Enter how many days did you spent in the hosptial? ")))
```
### def final_statement Function
  The def final statement collects all of the user's collected information and prints and calculates user data. Sum is used within the program to calculate the actual data entered into the function's equations. The function then executes an if statement, which outputs the total of all charges requested in the program in an orderly fashion. In addition, the function includes a "random.choice" line of code that displays a different nurse's name each time the code is used.
  ```
    room_charges = days_price * user_days

sum_total_inpatient = services_prices_sum + room_charges + medicine_prices_sum
    sum_total_outpatient = services_prices_sum + medicine_prices_sum

 random_FN = random.choice(nurse_first_name)
    random_LN = random.choice(nurse_last_name)

 if patient_status.lower() == "i":
        print(f"Room charges    $ {room_charges}")
        print(f"Labs & Services $ {services_prices_sum}")
        print(f"Medication      $ {medicine_prices_sum}")
        print(f"Total charges   $ {sum_total_inpatient}")
    else:
        print(f"Labs & Services $ {services_prices_sum}")
        print(f"Medication      $ {medicine_prices_sum}")
        print(f"Total charges   $ {sum_total_outpatient}")
```
# 8. Extras
To improve the look of the code and have a cleaner user interface we included special code that make the code more welcoming. The first line of code to improve user interface is "art_1 = text2art("Welcome", font="rnd-medium")" and " print("\nCalculating bill... ")".

# The Welcome Sign
When the user runs the code for the first time, they are greeted with a large welcome message and the hospital name "Welcome to a hospital project for ____ children hospital" underneath. This is a Python feature used to create text art, and it can also change the size of the string. In addition, each time the code is executed, the font of the welcome sign will change.
```
art_1 = text2art("Welcome", font="rnd-medium")

 def greeting(user_1, user_2, time_now):
    print("Welcome to a hospital project for _____ children hospital\nEnter 'd' to refer to documentation before going "
          "further! Enjoy\n")
```
# The Loading Bar
A loading bar was added to the user interface to give the user a visual representation of all of their information loading together before they get their results. To make the loading bar more realistic, a for loop on a "for in tqdm" was used to slow down how fast the loading bar will complete itself and it ranges from 0 to 100%, while "time.sleep" slows the code by a factor of two (0.2). Once the loading bar has finished loading, the program will print your final bill as well as the name of the nurse who assisted you.
```
 print("\nCalculating bill... ")

    for _ in tqdm(range(100)):
        time.sleep(.02)

    print("\t\t\t++++++++This is your final bill++++++++")
    print("\n")
    print(f"{today: %B %d, %Y}\t\t\t\t\tNurse: {random_FN}, {random_LN}")
```

