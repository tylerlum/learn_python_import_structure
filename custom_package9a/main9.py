"""
Test 9: Example that doesn't work on Python 2 or 3
        Imports a module that lives in a different directory from the directory that this file exists in
        Note: It doesn't work whether there is an __init__.py or not
"""

import custom_package9b.custom_math9

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_package9b.custom_math9.sqrt(float(value))))
