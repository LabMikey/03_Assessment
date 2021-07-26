# function goes here

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


# main routine goes here
budget = float_check("Budget: ", 0, 20)
