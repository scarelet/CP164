"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from utilities import list_test
from List_array import List

llist = List()

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

for each in foods:
    llist.append(each)

list_test(llist)
