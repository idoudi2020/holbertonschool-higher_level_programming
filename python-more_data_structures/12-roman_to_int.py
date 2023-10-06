#!/usr/bin/python3
def roman_to_int(roman_string):
    Roman_numerals = {'I': 1,'V': 5,  'X': 10, 'L': 50, 'C': 100, 'D': 500,  'M': 1000  }
    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = Roman_numerals.get(char, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result






































roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))