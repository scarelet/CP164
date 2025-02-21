"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""

from Deque_linked import Deque

deque = Deque()

for value in [1, 2, 3, 4, 5]:
    deque.insert_rear(value)
print("Deque after inserting values at rear:")
for value in deque:
    print(value, end=' ')
print()

for value in [-6, -7, -8, -9, -1]:
    deque.insert_front(value)
print("Deque after inserting values in the front:")
for value in deque:
    print(value, end=' ')
print()

front_value = deque.remove_front()
rear_value = deque.remove_rear()
print(
    f"Removed values from the front: {front_value}, Removed values from the rear: {rear_value}")

front_peek = deque.peek_front()
rear_peek = deque.peek_rear()
print(f"Peek front: {front_peek}, Peek rear: {rear_peek}")

print("Is the deque empty?", deque.is_empty())

print("Length of the current deque:", len(deque))

deque2 = Deque()
for value in [-2, -1, 0, 1, 2, 3, 4]:
    deque2.insert_rear(value)

print("Are the deques equal?", deque == deque2)


print("Iterating through the deque:")
for value in deque:
    print(value, end=' ')
print()
