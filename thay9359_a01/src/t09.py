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


from functions import matrixes_add

matrix_a = [
    [0, 1],
    [2, 3],
    [4, 5]
]

matrix_b = [
    [6, 7],
    [8, 9],
    [1, 0]
]

result_matrix = matrixes_add(matrix_a, matrix_b)

for row in result_matrix:
    print(row)

print()
