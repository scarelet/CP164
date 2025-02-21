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
from Queue_array import Queue

source_queue = Queue()

for i in range(10):
    source_queue.insert(i)


target1, target2 = source_queue.split_alt()

print("Target 1 Queue:")
for value in target1:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in target2:
    print(value, end=' ')
print()
