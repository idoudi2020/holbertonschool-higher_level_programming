#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = (abs(number) % 10) * (-1 if number < 0 else 1 )

if (last_digit == 0 ):
    print("Last digit of", number ,"is" ,last_digit, "and is 0" ) 
elif ( (last_digit < 6) and not 0 ): 
    print("Last digit of", number ,"is" ,last_digit, "and is less than 6 and not 0" )

else:
    print("Last digit of", number ,"is" ,last_digit, "and is greater than 5" )


"""
i can use this code also
# import random
# number = random.randint(-10000, 10000)
# last_digit = (abs(number) % 10) * (-1 if number < 0 else 1)
# print(f'Last digit of {number} is {last_digit} and','is 0' if last_digit == 0 else 'is greater than 5' if last_digit > 5 else 'is less than 6 and not 0')
"""
