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

original_list = List()
for value in range(1, 6):
    original_list.append(value)

# Display the original list order.
print("Original List:")
cur = original_list._front
while cur is not None:
    print(cur._value, end=" ")
    cur = cur._next
print()

# Reverse the list using the recursive method.
original_list.reverse_r()

# Display the reversed list order.
print("Reversed List:")
cur = original_list._front
while cur is not None:
    print(cur._value, end=" ")
    cur = cur._next
print()
