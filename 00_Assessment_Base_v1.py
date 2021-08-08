# function goes here
import pandas
import re


def float_check(question, error, num_type, lowest):
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
    print('Grams to Kilograms')



def unit_cost():
    gm = float(input('Enter a weight in Grams: '))
    get_cost = float(input('How much does it cost? '))
    kg = gm / 1000
    unit_price = get_cost / kg
    return unit_price

print_menu()
item = unit_cost()
print(item)
if budget <(item):
    print('Sorry you have insufficient funds.' )


