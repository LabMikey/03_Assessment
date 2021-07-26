# Checks for an integer more than 0
def float_check(question):

    error = "Please enter a whole number that is more than 99 grams"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = float(input(question))

            if response <= 99:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)



#Main rountine
weight = float_check ("Weight(Grams): ")

if weight < 100:
    print()
