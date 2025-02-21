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

from Food_utilities import get_vegetarian, read_foods
from Food import Food

file = open('foods.txt', 'r')
foods = read_foods(file)

veggie = get_vegetarian(foods)

for food in veggie:
    print(food)

file.close()
