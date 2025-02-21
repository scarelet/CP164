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

stack = Stack()

print("Is the stack empty?: ", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print("Is the stack empty ?: ", stack.is_empty())

top_element = stack.peek()
print("Top element: ", top_element)

popped_element = stack.pop()
print("Popped element: ", popped_element)

new_top_element = stack.peek()
print("New top element after popping: ", new_top_element)

print("Elements in the stack in order:")

for element in stack:
    print(element)
