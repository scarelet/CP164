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

from functions import file_analyze

fh = open("t04.txt", "r", encoding="utf-8")

upp, low, dig, whi, rem = file_analyze(fh)

print(f"""
Uppercase:  {upp}
Lowercase:  {low}
Digits:     {dig}
WhiteSpace: {whi}
Remaining:  {rem}
""")
