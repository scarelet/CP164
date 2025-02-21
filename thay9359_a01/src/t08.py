"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thay9359@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import matrix_stats

matrix = [
    [4, 3, 4.8, 7.2],
    [4.9, 5.6, 2.3],
    [6.8, 1.9, 3.7]
]

small, large, total, average = matrix_stats(matrix)
print("Smallest:", small)
print("Largest:", large)
print("Total:", total)
print("Average:", average)
print()
