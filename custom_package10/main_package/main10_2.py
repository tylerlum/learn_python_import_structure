"""
Test 10.2: Example that does work on Python 2 or 3 run from anywhere
           It doesn't depend on the caller location, as this uses the absolute path to this file when adding to path
           Imports a module that lives in a different directory from the directory that this file exists in
           Note: __init__.py is needed in custom_package9b for this to work in Python 2
"""
import os
import sys
sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import math_package.custom_math10

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, math_package.custom_math10.sqrt(float(value))))
