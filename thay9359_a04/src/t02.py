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
from Queue_circular import Queue

queue_1 = Queue()
queue_2 = Queue()


for element in [1, 2, 3, 4, 5]:
    queue_1.insert(element)
    queue_2.insert(element)


if queue_1.__eq__(queue_2):
    print("Both queue are equal.")
else:
    print("The queue are not equal.")


queue_2.remove()
queue_2.insert(6)


if queue_1.__eq__(queue_2):
    print("Both queue are equal.")
else:
    print("After altering, both queue are not equal.")
