#!/usr/bin/python3
# -*- coding: utf-8 -*-
for x in range(97, 123):
    print("{:c}".format(x), end="")


"""
we cane use this also
(f'{chr(x)}', end="")
("{}".format(chr(x)), end="")
"""
