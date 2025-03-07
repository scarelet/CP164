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
from Food_utilities import calories_by_origin

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

calories_1 = calories_by_origin(foods, 1)

calories_2 = calories_by_origin(foods, 2)

calories_3 = calories_by_origin(foods, 3)

print(f""" 
Average calories in Chinese food is: {calories_1} 
Average calories in Indian food is: {calories_2} 
Average calories in Ethiopian foods is: {calories_3} 

""")
