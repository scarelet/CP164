"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""

from List_linked import List

my_list = List()
my_list.append("red")
my_list.append("yellow")
my_list.append("orange")
my_list.append("green")

found_item = my_list.find("red")
print("Found item:", found_item)

index_of_cherry = my_list.index("orange")
print("Index of 'orange':", index_of_cherry)

contains_apple = "blue" in my_list
print("Is 'blue' in the list?", contains_apple)
