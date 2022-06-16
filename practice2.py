#2. Write a Python program to find the sum of all items in a dictionary?
dict1 = {'A': [1, 3, 5, 4],
         'B': [4, 6, 8, 10],
         'C': [6, 12, 4, 8],
         'D': [5, 7, 2]}
sum = 0
for val in dict1.values():
    for ele in val:
        sum = sum + ele
print(f"total sum is: {sum}")