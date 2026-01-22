"""
main.py
"""

from colors import C
from queue_system import QueueSystem

sequence = [C.g, C.r, C.p, C.b, C.w]
qs = QueueSystem(sequence)

print()
print("q : dump current primary")
print("w : swap priimary and secondary")
print("other : exit")
print()

while True:
    i = input(f"{qs} : ")
    if i == "q":
        qs.dump()
    elif i == "w":
        qs.w()
    else:
        break
