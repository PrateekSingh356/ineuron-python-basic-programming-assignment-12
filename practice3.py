#3. Write a Python program to Merging two Dictionaries?
dict1 = {'A': [1, 3, 5, 4],
         'B': [4, 6, 8, 10],
         'C': [6, 12, 4, 8],
         'D': [5, 7, 2,4]}
dict2 = {'E': [1, 3, 5, 4],
         'F': [4, 6, 8, 10],
         'G': [6, 12, 4, 8],
         'H': [6, 12, 4,5]}
def merge(dict1,dict2):
    return dict1.update(dict2)

merge(dict1,dict2)
print(dict1)