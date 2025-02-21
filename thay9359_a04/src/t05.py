"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thaayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)


split_key = 4


higher_priority, lower_or_equal_priority = pq_split_key(pq, split_key)

print("Target 1 Queue:")
for value in higher_priority:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in lower_or_equal_priority:
    print(value, end=' ')
print()
