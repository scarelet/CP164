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

my_list.append(10)
my_list.append(20)
my_list.append(30)

second_item = my_list[1]
print(f"Second item in the list: {second_item}")

print("Setting second item to 25...")
my_list[1] = 45

try:
    print("Attempting to access index out of range:")
    my_list[5]
except AssertionError as e:
    print(f"Error: {e}")

try:
    print("Attempting to set index out of range:")
    my_list[5] = 50
except AssertionError as e:
    print(f"Error: {e}")
