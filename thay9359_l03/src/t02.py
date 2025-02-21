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


print("Inserting elements into the queue:")
for element in elements:
    q.insert(element)

print(f"Queue contains: {[val for val in q]}")

if not q.is_empty():
    front_element = q.peek()
    print(f"\nPeeking at the front element: {front_element}")

print("\nRemoving elements from the queue:")
while not q.is_empty():
    removed_element = q.remove()
    print(f"Removed {removed_element} from the queue.")
    if not q.is_empty():
        next_element = q.peek()
        print(f"Next element to be removed: {next_element}")
    else:
        print("The queue is empty.")
    print(f"Queue contains: {[val for val in q]}")
