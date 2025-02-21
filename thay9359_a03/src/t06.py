"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import postfix

expressions = [
    "12 5 -",
    "4 5 + 12 * 2 3 * -",
    "7 2 + 3 /"
]

for expr in expressions:
    result = postfix(expr)
    print(f"'{expr}' evaluates to {result}")
