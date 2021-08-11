# Unit price conversion
#Functions
def print_menu():
    print('Grams to Kilograms')

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

def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response == "":
            print("{}.  \nPlease try again.\n".format(error))

        return response



weight = num_check ("Weight(Grams): ", "Please enter a number more than 10", int, 10)
print("The weight is {}".format(weight))
cost = num_check("Cost: $", "Please enter a valid number", float, 0)
print("The cost is ${} in grams". format(cost))
# weight has been changed to kilograms here
unit_price = cost / (weight / 1000)
print("$", unit_price, "Per Kilo")


