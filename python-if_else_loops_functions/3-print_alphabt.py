#!/usr/bin/python3

for x in range(97, 123):
    if (x == 101 or x == 113):
        continue
    print("{:c}".format(x), end='')

    """
for x in range(1, 10):
    if (x != 101 or x != 113):
        print("{:d}".format(x), end='')

  """      
