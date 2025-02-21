"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(1)
pq.insert(50)
pq.insert(25)
pq.insert(12)

highest_priority_value = pq.peek()
print("Highest priority value is:", highest_priority_value)


pq2 = Priority_Queue()

pq2.insert("Grapes")
pq2.insert("Orange")
pq2.insert("Cherry")

highest_priority_value2 = pq2.peek()
print("Highest priority value is:", highest_priority_value2)
