# Checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 10 grams"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 10:
                print(error)
            else:
                return(response)

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

#Main rountine
weight = int_check ("Weight(Grams): ")
print("The weight is {}".format(weight))

cost = int_check("Cost: $")

# if weight < 100:
#     print()

