#7. Write a Python program to sort Python Dictionaries by Key or Value?
key_value = {}

key_value[5] = 10
key_value[3] = 8
key_value[6] = 77
key_value[4] = 23
key_value[2] = 9
key_value[1] = 43

print("sorting on the basis of keys")

for i in sorted(key_value):
    print((i, key_value[i]), end=" ")