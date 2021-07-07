budget = tool_list ={'Sea Salt Crakers': 2,
            'Griffins Snax': 2.5,
            'Pizza Shapes': 3.3,
            'Arnotts Cheds': 3.99,
            'Rosemary Wheat': 2,
            'Orginal Rice Crakers': 1.65
}



profit = 0





budget = int(input("Budget: "))  # replace with functions

if budget < 2:
        tool_list = 'Sea Salt Crakers'
elif budget < 2.5:
        tool_list = 2.5
elif budget < 3.3:
        tool_list = 3.3
elif budget < 3.99:
        tool_list = 3.99
else:
        tool_list = 6.5

print("{} : ${:.2f}".format(budget, tool_list))

print("Profit from tickets: ${:.2f}".format(profit))