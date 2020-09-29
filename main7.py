"""
Test 7: Example that only works on Python3.3+, not Python2.
        Imports a module that lives in a directory in a directory that is in the same directory as this file
        Note: The lower level directory has an __init__.py file, but not the higher level directory
        This is fine for Python3.3+, which can still use it as a namespace package, but not a regular package
        For Python2, this does not work.
"""

import custom_package7.nested_package.custom_math7

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_package7.nested_package.custom_math7.sqrt(float(value))))
