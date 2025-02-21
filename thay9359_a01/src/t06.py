"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import is_valid

variable_name = "2var"
valid = is_valid(variable_name)

if valid:
    print(f"{variable_name} is a valid Python variable name.")
else:
    print(f"{variable_name} is a invalid Python variable name.")
