"""
Test 2: Simple working example that imports a module in the same directory as this file
"""

import custom_math2

value = input("Please enter a number to be square rooted: ")
print("{} square rooted = {}".format(value, custom_math2.sqrt(float(value))))
