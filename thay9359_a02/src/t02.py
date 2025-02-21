"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Food_utilities import average_calories

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

calories = average_calories(foods)

print(f"Average calories: {calories}")
