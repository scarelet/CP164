"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
from functions import is_palindrome

test = ["A man, a plan, a canal: Panama",
        "racecar", "hello", "No 'x' in Nixon"]

for s in test:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")
