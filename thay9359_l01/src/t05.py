"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
from Food_utilities import read_foods

fh = open("foods.txt", "r")

items = read_foods(fh)

for every in items:
    print(every)
    print()
