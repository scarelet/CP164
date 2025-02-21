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
from utilities import stack_test

source_data = Stack()

source_data.push(10)
source_data.push(20)
source_data.push(30)
source_data.push(40)
source_data.push(50)

stack_test(source_data)

print("\nTesting with an empty source list:")
empty_source_data = Stack()
stack_test(empty_source_data)
