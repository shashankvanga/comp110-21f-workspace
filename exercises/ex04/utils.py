"""List utility functions."""

__author__ = "730489843"


def all(one: list[int], two: int) -> bool:
    """Checks if all the ints in a list match a given int."""
    i: int = 0
    if len(one) == 0:
        return False
    while i < len(one):
        check: int = one[i]
        if check != two:
            return False
        i += 1
    
    return True


def is_equal(one: list[int], two: list[int]) -> bool:
    """Checks if all the ints in a list match the ints of another list."""
    size_1: int = len(one)
    size_2: int = len(two)
    if size_1 != size_2:
        return False
    
    i: int = 0

    while i < size_1:
        check_one: int = one[i]
        check_two: int = two[i]
        if check_one != check_two:
            return False
        i += 1
    
    return True


def max(x: list[int]) -> int:
    """Returns the largest int from a list of ints."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = x[0]
    i: int = 1
    while i < len(x):
        if x[i] > maximum:
            maximum = x[i]
        i += 1 
    return maximum