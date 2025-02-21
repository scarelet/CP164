"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
from List_array import List

my_list = List()

my_list.append(10)
my_list.append(30)
my_list.append(30)
my_list.append(30)
my_list.append(10)

index_of_20 = my_list.index(230)
print(f"Index for the first occurrence of '20': {index_of_20}")

found_value = my_list.find(40)
print(f"Value found for '40': {found_value}")

contains_20 = 20 in my_list
print(f"Is '20' in the list? {contains_20}")

count_of_10 = my_list.count(10)
print(f"The # of '10' in the list: {count_of_10}")

max_value = my_list.max()
print(f"Maximum value in the list: {max_value}")

min_value = my_list.min()
print(f"Minimum value in the list: {min_value}")
