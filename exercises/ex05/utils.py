"""List utility functions part 2."""

__author__ = "730489843"


def only_evens(even: list[int]) -> list[int]:
    """Function that returns only even integers from a list of integers."""
    i: int = 0
    evens: list[int] = []
    while i < len(even):
        check: int = even[i]
        if check % 2 == 0:
            evens.append(check)
        i += 1
    return evens

# print(only_evens([1, 3, 9]))


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns a validated subset of a given list between the start and end values."""
    subset: list[int] = []
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return subset
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    i: int = start

    while i < end:
        subset.append(a_list[i])
        i += 1
    return subset

# print(sub([1, 2, 3, 4], 2, 2))


def concat(one: list[int], two: list[int]) -> list[int]:
    """Returns a new concatenated list using two given lists."""
    new_list: list[int] = []

    i: int = 0

    while i < len(one):
        new_list.append(one[i])
        i += 1

    n: int = 0

    while n < len(two):
        new_list.append(two[n])
        n += 1
    
    return new_list

# print(concat(two=[1, 2, 3], one=[4, 5, 6]))