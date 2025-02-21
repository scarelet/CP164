"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack

source_stack = Stack()

source_stack._values.extend([4, 6, 8])

print(f"Before: {source_stack._values}")

source_stack.reverse()

print(f"After: {source_stack._values}")
