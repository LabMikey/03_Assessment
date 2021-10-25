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

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can’t be blank, "
                 "please enter your name")



# main routine goes here
budget = float_check("Budget: ", 0, 100)

# Column set up
all_items = []
all_weight = []
all_cost = []
all_unit_cost = []

# table set up
Price_tool_dict = {
    'Items': all_items,
    'weight': all_weight,
    'Cost': all_cost,
    'Unit Price': all_unit_cost
}

# Loop to get the Item name
item_name = ""

while item_name.lower() != "xxx":
    print()

    # Get name of item
    item_name = not_blank("Item Name: ")
    # End loop if the exit code is entered
    if item_name == "xxx":
        break

    # Unit price conversion
    weight = num_check ("Weight(Grams): ", "Please enter a number more than 10", int, 10)
    print("The weight is {}".format(weight))
    cost = num_check("Cost: $", "Please enter a valid number", float, 0)
    print("The cost is ${} in grams". format(cost))
    # weight has been changed to kilograms here
    unit_price = cost / (weight / 1000)
    print("${:.2f} per kilo".format(unit_price))

    print("\n\n")
    if budget < unit_price:
        print('Sorry you have insufficient funds.' )

    all_items.append(item_name)
    all_weight.append(weight)
    all_cost.append(cost)
    all_unit_cost.append("${:.2f} per kilo".fomatunit_price)

movie_frame = pandas.DataFrame(Price_tool_dict)
print(movie_frame)
