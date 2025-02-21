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

playlist = List()

playlist.prepend("No Blueberries - DPR Ian")

playlist.append("Trust Issues - Drake")

playlist.insert(1, "After Hours - Weeknd")

for all in playlist:
    print(all)
