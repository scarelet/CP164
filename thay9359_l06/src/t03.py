"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
from List_linked import List

my_list = List()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(40)

count_20 = my_list.count(20)
print("The value '20' appears", count_20, "times in the list.")

max_value = my_list.max()
print("Maximum value in the list:", max_value)

min_value = my_list.min()
print("Minimum value in the list:", min_value)
