# learn_python_import_structure
The purpose of this repository is to test out different options for importing modules and packages.

Importing python modules is easy when it works, but it can be frustrating when it doesn't. In this repository are many `main<XX>.py` files that attempt to import a custom math function in a different structure, including

* Custom math function in the same directory as main

* Custom math function in a directory that is in the same directory as main

* Custom math function in a nested directory that is in the same directory as main

* Custom math function in a sibling directory of main

This can be tested by running commands like:

`python2 main1.py`, or `python3 main4.py`, or `python2 custom_package9a/main9_2.py`.

To understand what each main file is testing and what the expected output should be, please look at the docstring at the top of each main file.

![image](https://user-images.githubusercontent.com/26510814/94515670-f03c9d00-01d8-11eb-8be7-d820242c7649.png)

_Example of a situation in which the import structure doesn't work for Python2 but works for Python3_
