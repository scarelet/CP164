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
from utilities import stack_to_array

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

target = []

stack_to_array(stack, target)

print("Is the stack empty: ",
      stack.is_empty())

print("Elements in the target array:", target)
