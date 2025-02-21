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

from functions import is_leap_year

year_to_check = 2024
leap_year = is_leap_year(year_to_check)

if leap_year:
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
