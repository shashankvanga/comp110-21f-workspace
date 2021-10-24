"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730489843"


def test_only_evens_edge() -> None:
    """Edge case test."""
    even: list[int] = []
    assert only_evens(even) == []


def test_only_evens_use_one() -> None:
    """Use case test one."""
    even: list[int] = [1, 2, 3, 4]
    assert only_evens(even) == [2, 4]


def test_only_evens_use_two() -> None:
    """Use case test two."""
    even: list[int] = [22, 23, 24, 25]
    assert only_evens(even) == [22, 24]


def test_sub_edge() -> None:
    """Edge case test."""
    a_list: list[int] = []
    start: int = 2
    end: int = 3
    assert sub(a_list, start, end) == []


def test_sub_use_one() -> None:
    """Use case test one."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 2
    end: int = 4
    assert sub(a_list, start, end) == [3, 4]


def test_sub_use_two() -> None:
    """Use case test two."""
    a_list: list[int] = [23, 24, 25, 26]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [24, 25]


def test_concat_edge() -> None:
    """Edge case test."""
    one: list[int] = []
    two: list[int] = []
    assert concat(one, two) == []


def test_concat_use_one() -> None:
    """Use case test one."""
    one: list[int] = [1, 2, 3]
    two: list[int] = [4, 5, 6]
    assert concat(one, two) == [1, 2, 3, 4, 5, 6]


def test_concat_use_two() -> None:
    """Use case test two."""
    one: list[int] = [23, 24, 25]
    two: list[int] = [26, 27, 28]
    assert concat(one, two) == [23, 24, 25, 26, 27, 28]