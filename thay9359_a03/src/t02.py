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

source1 = Stack()
source2 = Stack()
target = Stack()

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

target.push(1)
target.push(2)
target.push(3)

target.combine(source1, source2)

print(target._values)
