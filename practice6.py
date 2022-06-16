#6. Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict
def checkOrder(input, pattern):
    # create empty OrderedDict
    # output will be like {'a': None,'b': None, 'c': None}
    dict = OrderedDict.fromkeys(input)

    ptrlen = 0
    for key, value in dict.items():
        if (key == pattern[ptrlen]):
            ptrlen = ptrlen + 1

        # check if we have traverse complete
        # pattern string
        if (ptrlen == (len(pattern))):
            return 'true'

    return 'false'

input = 'engineers rock'
pattern = 'er'
print(checkOrder(input, pattern))