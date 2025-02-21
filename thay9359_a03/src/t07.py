"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_maze

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F', 'X'],
    'F': ['G'],
    'G': ['C']
}

print(maze)


print(stack_maze(maze))
