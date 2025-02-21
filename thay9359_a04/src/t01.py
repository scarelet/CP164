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

queue = Queue()

print("Inserting elements into the queue...")
for i in range(5):
    queue.insert(i)
    print(f"Insert {i} into the queue.")

if queue.is_empty():
    print("The queue is empty.")
else:
    print("The queue is not empty.")

if queue.is_full():
    print("The queue is full.")
else:
    print("The queue is not full.")

first_element = queue.peek()
print(f"First element in the queue is: {first_element}")

removed_element = queue.remove()
print(f"Removed element {removed_element} from the queue.")

print(f"The queue currently has {len(queue)} elements.")

another_queue = Queue()
for i in range(5):
    another_queue.insert(i)

if queue == another_queue:
    print("The queues are equal.")
else:
    print("The queues are not equal.")

print("Iterating over the queue:")
for value in queue:
    print(value)
