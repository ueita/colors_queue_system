"""
Module for class C (printable strings for the colors)
"""

class C:
    """
    Class C

    +-----------+--------+------------+
    | Attribute | Color  | Name       |
    +-----------+--------+------------+
    | g         | Green  | Calibrum   |
    | r         | Red    | Severum    |
    | p         | Purple | Gravitum   |
    | b         | Blue   | Infernum   |
    | w         | White  | Crescendum |
    +-----------+--------+------------+
    """

    g : str = "\033[96mCalibrum\033[0m"
    r : str = "\033[91mSeverum\033[0m"
    p : str = "\033[94mGravitum\033[0m"
    b : str = "\033[95mInfernum\033[0m"
    w : str = "\033[97mCrescendum\033[0m"

if __name__ == "__main__":
    print(C.g)
    print(C.r)
    print(C.p)
    print(C.b)
    print(C.w)
