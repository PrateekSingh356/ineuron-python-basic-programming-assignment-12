#4. Write a Python program to convert key-values list to flat dictionary?
my_dict = {'month_num' : [1, 2, 3, 4, 5, 6], 'name_of_month' : ['Jan', 'Feb', 'March', 'Apr', 'May', 'June']}
print("The dictionary is : ")
print(my_dict)
my_result = dict(zip(my_dict['month_num'], my_dict['name_of_month']))
print("The flattened dictionary is: ")
print(my_result)