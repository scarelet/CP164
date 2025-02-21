"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-03-02"
-------------------------------------------------------
"""
# Imports

from List_linked import List

list1 = List()
list2 = List()


for value in [1, 2, 3, 4, 5]:
    list1.append(value)
    list2.append(value)


identical = list1.is_identical_r(list2)
print(f"The lists are{' ' if identical else ' not '}identical.")


list2.append(6)
identical = list1.is_identical_r(list2)
print(f"""After adding an element to list2, the lists are 
{' ' if identical else ' not '} identical.
      """)


list3 = List()
for value in [5, 4, 3, 2, 1]:
    list3.append(value)


identical = list1.is_identical_r(list3)
print(f"The lists are{' ' if identical else ' not '}identical.")
