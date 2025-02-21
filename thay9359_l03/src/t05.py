"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Navina Thayaruban
ID:     169069359
Email:  thay9359@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(40)
pq.insert(20)
pq.insert(10)

while not pq.is_empty():
    highest_priority_value = pq.remove()
    print("Removed:", highest_priority_value)

print()

q = Priority_Queue()

q.insert("Cherry")
q.insert("Grapes")
q.insert("Apple")

while not q.is_empty():
    highest_priority_value1 = q.remove()
    print("Removed:", highest_priority_value1)
