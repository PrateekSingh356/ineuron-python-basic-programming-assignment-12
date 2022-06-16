#1. Write a Python program to Extract Unique values dictionary values?
dict1 = {'A': [1, 3, 5, 4],
         'B': [4, 6, 8, 10],
         'C': [6, 12, 4, 8],
         'D': [5, 7, 2]}
res = []
print("The original dictionary is : ", dict1)
for val in dict1.values():
    for ele in val:
        res.append(ele)
print("The unique values list is : ", set(res))