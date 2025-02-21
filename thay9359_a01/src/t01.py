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
from functions import clean_list

values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4,
          3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]

print(f"List before: {values}")

clean_list(values)

print(f"List after: {values}")
