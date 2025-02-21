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
from Queue_array import Queue

q = Queue()

elements = [10]

print("Insert elements into the queue:")
for element in elements:
    print(f"Insert {element} into the queue.")
    q.insert(element)
    print(f"Queue contains: {[val for val in q]}")
