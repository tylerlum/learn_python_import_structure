"""
Test 3: Example that only works on Python3.3+, not Python2.
        Imports a module that lives in a directory that is in the same directory as this file
        Note: The directory that holds to modules does not have a __init__.py file, so it is not a package
        This is fine for Python3.3+, which can still use it as a namespace package, but not a regular package
        For Python2, this does not work.
"""

import custom_package3.custom_math3

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_package3.custom_math3.sqrt(float(value))))
