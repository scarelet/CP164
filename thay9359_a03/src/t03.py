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
from functions import stack_reverse
from Stack_array import Stack

source_stack = Stack()


source_stack.push(1)
source_stack.push(2)
source_stack.push(3)

print(f"Before: {source_stack._values}")

stack_reverse(source_stack)

print(f"After: ")

while not source_stack.is_empty():
    print(source_stack.pop())
