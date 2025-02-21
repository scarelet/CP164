"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Your Name
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""

from List_linked import List

my_list = List()
my_list.append("red")
my_list.append("orange")
my_list.append("yellow")
my_list.append("green")

first_item = my_list.peek()
print("First item (peeked):", first_item)

removed_item = my_list.remove("orange")
print("Removed item:", removed_item)
