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
from functions import stack_combine

source1 = Stack()
source2 = Stack()

source1.push(5)
source1.push(8)
source1.push(12)
source1.push(8)

source2.push(3)
source2.push(6)
source2.push(1)
source2.push(7)
source2.push(9)
source2.push(14)

combined = stack_combine(source1, source2)

for item in combined:
    print(item)
