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
from Food_utilities import write_foods, get_food

fh = open("foods.txt", "a", encoding="utf-8")


foods = []

foods.append(get_food())

foods.append(get_food())

foods.append(get_food())

write_foods(fh, foods)
