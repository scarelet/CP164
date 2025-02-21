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
from List_array import List
from utilities import list_to_array
from utilities import array_to_list


llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)
print("After array_to_list:")
for value in llist:
    print(value, end=' ')
print()

target = []
list_to_array(llist, target)
print("After list_to_array:", target)
print("Empty after transfer:", llist.is_empty())
