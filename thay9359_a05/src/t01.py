"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
from List_array import List
from Food_utilities import read_foods
from copy import deepcopy
from Food import Food

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)
food_list = List()
for food in foods:
    food_list.append(food)


if len(food_list) > 0:
    print("Get item:", food_list[0])

food_list.clean()
print("List after clean:", [str(food) for food in food_list])


list1 = List()
list1.append(foods[0])
list2 = List()
list2.append(foods[1])
food_list.combine(list1, list2)
print("List after combine:", [str(food) for food in food_list])

# Test intersection
list1 = deepcopy(food_list)
list2 = deepcopy(food_list)
list1.intersection(list1, list2)
print("List after intersection:", [str(food) for food in food_list])


food_list.prepend(Food("Test Food", 0, True, 100))
print("List after prepend:", [str(food) for food in food_list])


if not food_list.is_empty():
    food_list.remove_front()
print("List after remove_front:", [str(food) for food in food_list])


if len(food_list) > 0:
    food_list.remove_many(food_list[0])
print("List after remove_many:", [str(food) for food in food_list])


if len(food_list) > 0:
    list1, list2 = food_list.split()
    print("List 1 after split:", [str(food) for food in list1])
    print("List 2 after split:", [str(food) for food in list2])


if len(food_list) > 0:
    list1, list2 = food_list.split_alt()
    print("List 1 after split_alt:", [str(food) for food in list1])
    print("List 2 after split_alt:", [str(food) for food in list2])


list1 = List()
list2 = List()
list1.append(foods[0])
list2.append(foods[1])
food_list.union(list1, list2)
print("List after union:", [str(food) for food in food_list])


list1 = List()
list1.append(foods[0])
list2 = List()
list2.append(foods[0])
print("List1 equal List2:", list1 == list2)


for food in food_list:
    print(food)
