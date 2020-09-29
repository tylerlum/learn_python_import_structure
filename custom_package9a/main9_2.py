"""
Test 9.2: Example that does work on Python 2 or 3 ONLY if run from the custom_package9a directory
          It adds <current_directory_of_caller>/../ to the Python path, so it needs to be run from there
          Imports a module that lives in a different directory from the directory that this file exists in
          Note: __init__.py is needed in custom_package9b for this to work in Python 2
"""
import os
import sys
sys.path.insert(1, "../")

import custom_package9b.custom_math9

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_package9b.custom_math9.sqrt(float(value))))
