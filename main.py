"""
main.py
"""

from colors.colors import C
from queue_system.queue_system import QueueSystem

sequence = [C.g, C.r, C.p, C.b, C.w]
qs = QueueSystem(sequence)

print(
    "q : dump current main\n"
    "w : swap main and off-hand\n"
    "other : exit\n"
)

while True:
    cmd = input(f"{qs} : ").strip().lower()
    if cmd == "q":
        qs.dump()
    elif cmd == "w":
        qs.w()
    else:
        break
