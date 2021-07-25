def float_check(question):

    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

tool_list_1 =[["Sea Salt Crakers", "$2"]]
tool_list_2 =[["Griffins Snax", "$2.5"]]
tool_list_3 =[["Pizza Shapes", "$3.3"]]
tool_list_4 =[["Arnotts Cheds", "$3.99"]]
tool_list_5 =[["Rosemary Wheat", "$2"]]
tool_list_6 =[["Orginal Rice Crakers", "$1.65"]]


budget = float_check("Budget: ")  # replace with functions

if budget < 1.0:
        tool_list_6 = []
elif budget < 2.0:
        tool_list_1 = []
elif budget < 2.5:
        tool_list_2 = []
elif budget < 3.3:
        tool_list_3 = []
elif budget < 3.99:
        tool_list_4 = []
else:
        tool_list_5 = []

print("{} : {}".format(budget, tool_list_1, tool_list_2, tool_list_3, tool_list_4, tool_list_5, tool_list_6))

