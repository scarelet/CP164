"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-03-02"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list1 = List()
list2 = List()


for value in [1, 3, 5, 7]:
    list1.append(value)


for value in [2, 4, 6, 8, 0]:
    list2.append(value)


union_list = List()


union_list.union_r(list1, list2)


print("Union of list1 and list2:")
current = union_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
