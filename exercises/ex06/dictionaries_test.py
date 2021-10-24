"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730489843"


def test_invert_edge() -> None:
    """Edge case test."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_invert_use_one() -> None:
    """Use case one."""
    x: dict[str, str] = {"Shashank": "Vanga"}
    assert invert(x) == {"Vanga": "Shashank"}


def test_invert_use_two() -> None:
    """Use case two."""
    x: dict[str, str] = {"Sai": "Kaza"}
    assert invert(x) == {"Kaza": "Sai"}


def test_favorite_color_edge() -> None:
    """Edge case test."""
    color: dict[str, str] = {}
    assert favorite_color(color) == ""


def test_favorite_color_use_one() -> None:
    """Use case one."""
    color: dict[str, str] = {"Shashank": "Blue", "Sai": "Blue"}
    assert favorite_color(color) == "Blue"


def test_favorite_color_use_two() -> None:
    """Use case two."""
    color: dict[str, str] = {"Shashank": "Blue", "Sai": "Green"}
    assert favorite_color(color) == "Blue"


def test_count_edge() -> None:
    """Edge case test."""
    number: list[str] = []
    assert count(number) == {}


def test_count_use_one() -> None:
    """Use case one."""
    number: list[str] = ["a", "b", "a", "c"]
    assert count(number) == {"a": 2, "b": 1, "c": 1}


def test_count_use_two() -> None:
    """Use case two."""
    number: list[str] = ["a", "b", "a", "b"]
    assert count(number) == {"a": 2, "b": 2}