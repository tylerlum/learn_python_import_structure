"""
Test 4: Example that works on Python 2 and 3
        Imports a module that lives in a directory that is in the same directory as this file
        Note: The directory that holds to modules does have a __init__.py file, so it is a package
        Therefore, this file is able to find that package and import the module inside the package
"""

import custom_package4.custom_math4

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_package4.custom_math4.sqrt(float(value))))
