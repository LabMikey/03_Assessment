# function goes here
import pandas
import re


def float_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

       # ask user for Budget and check it is valid
        try:
            response = float(input(question))

            if low_num < response < high_num:
                return response
            else:
                print(error)

       # If an interger is not entered, display an error
        except ValueError:
            print(error)

def num_check(question, error, num_type, lowest):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= lowest:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# main routine goes here
budget = float_check("Budget: ", 0, 20)

# Unit price conversion
# Functions
def print_menu():
    print()
    print()


weight = num_check ("Weight(Grams): ", "Please enter a number more than 10", int, 10)
print("The weight is {}".format(weight))
cost = num_check("Cost: $", "Please enter a valid number", float, 0)
print("The cost is ${} in grams". format(cost))
# weight has been changed to kilograms here
unit_price = cost / (weight / 1000)
print("$", unit_price, "Per Kilo")

print (print_menu())
if budget <(unit_price):
    print('Sorry you have insufficient funds.' )


