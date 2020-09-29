"""
Test 8: Example that works on Python 2 and 3
        Imports a module that lives in a directory in a directory that is in the same directory as this file
        Note: Both the lower level directory and higher level directory have an __init__.py file
"""

import custom_package8.nested_package.custom_math8

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_package8.nested_package.custom_math8.sqrt(float(value))))
