# Unit price conversion
#Functions
def print_menu():
    print('Grams to Kilograms')

def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def unit_cost():
    gm = float(input('Enter a weight in Grams: '))
    get_cost = float(input('How much does it cost? '))
    kg = gm / 1000
    unit_price = get_cost / kg
    return unit_price
    print('You entered {} Grams; ' 'Weight in KG: {} Kilograms'.format(gm, kg))


print_menu()
item = unit_cost()
print(item)


