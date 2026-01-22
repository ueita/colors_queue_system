"""
Module for class QueueSystem (system for representing the queue)
"""

class QueueSystem:
    """
    Class QueueSystem
    """
    def __init__(self, seq : list[str]) -> None:
        self.seq = seq
        return

    def __str__(self) -> str:
        if len(self.seq) <= 2:
            return f"[ {' - '.join(self.seq)} ]"
        return f"[ {' - '.join(self.seq[:2])} ] " + " ".join(self.seq[2:])

    def w(self) -> "QueueSystem":
        """w"""
        if len(self.seq) >= 2:
            self.seq[0], self.seq[1] = self.seq[1], self.seq[0]
        return self

    def dump(self) -> "QueueSystem":
        """dump"""
        if self.seq:
            self.seq.append(self.seq.pop(0))
        self.w()
        return self

if __name__ == "__main__":
    print(QueueSystem(["1","2","3","4","5"]))
