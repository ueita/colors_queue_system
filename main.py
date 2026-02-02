"""
main.py
"""

from colors.colors import C
from queue_system.queue_system import QueueSystem

sequence = [C.g, C.r, C.p, C.b, C.w]
qs = QueueSystem(sequence)

print("q : dump current main")
print("w : swap main and off-hand")
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
