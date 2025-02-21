"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Navina Thayaruban
ID:     169069359
Email:  thay9359@mylaurier.ca
__updated__ = '2024-01-20'
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = [10, 20, 30, 40, 50]

print("Source array before:", source)

array_to_stack(stack, source)

print("Source array after: ", source)

print("Elements in the stack in order:")
for element in stack:
    print(element)
