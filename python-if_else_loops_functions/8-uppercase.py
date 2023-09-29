#!/usr/bin/python3
def uppercase(str):
    for str1 in str:
        if ord(str1) in range(97, 123):
            i = ord(str1) - 32
        else:
            i = ord(str1)
        print("{:c}".format(i), end='')
    print("")
