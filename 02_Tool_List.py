tool_list_1 =[["Sea Salt Crakers", "2"]]
tool_list_2 =[["Griffins Snax", "2.5"]]
tool_list_3 =[["Pizza Shapes", "3.3"]]
tool_list_4 =[["Arnotts Cheds", "3.99"]]
tool_list_5 =[["Rosemary Wheat", "2"]]
tool_list_6 =[["Orginal Rice Crakers", "1.65"]]




profit = 0




budget = float(input("Budget: "))  # replace with functions

if budget < 1:
        print(tool_list_6)
elif budget < 2:
        print(tool_list_1)
elif budget < 2.5:
        print(tool_list_2)
elif budget < 3.3:
        print(tool_list_3)
elif budget < 3.99:
        print(tool_list_4)
else:
        tool_list = 6.5

print("{} : {}".format(budget, tool_list_1, tool_list_2, tool_list_3, tool_list_4, tool_list_5, tool_list_6))

print("Profit from tickets: ${:.2f}".format(profit))