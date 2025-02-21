"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
from List_array import List

my_list = List()

print("Elements appending to the list...")
my_list.append(49)
my_list.append(50)
my_list.append(60)
print(f"List after appends: {[value for value in my_list]}")

print("\nInserting a element at index 1...")
my_list.insert(1, 15)
print(f"List after insert: {[value for value in my_list]}")

print("\nRemoving the element '20'...")
removed_value = my_list.remove(20)
print(f"Removed value: {removed_value}")
print(f"List after removal: {[value for value in my_list]}")

print("\nAttempting to remove a non-existent element '40'...")
result = my_list.remove(30)
print(f"Result of removal: {result}")
print(f"List after failed removal attempt: {[value for value in my_list]}")
