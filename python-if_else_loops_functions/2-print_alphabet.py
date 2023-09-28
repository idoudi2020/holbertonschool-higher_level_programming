#!/usr/bin/python3
# -*- coding: utf-8 -*-
for x in  range(97,123):
    print("{:c}".format(x), end="")

"""
same code avec 
print(f'{chr(x)}', end="")
print("{}".format(chr(x)), end="")
"""
