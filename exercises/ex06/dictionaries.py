"""Practice with dictionaries."""

__author__ = "730489843"


# Define your functions below
def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns inverted keys and values of a given dictionary."""
    y: dict[str, str]
    y = dict()
    for key in x:
        value = x[key]
        if value in y:
            raise KeyError
        else:
            y[value] = key
    return y


def favorite_color(color: dict[str, str]) -> str:
    """Prints favorite color from a list of colors."""
    frequency_dict: dict[str, int]
    frequency_dict = dict()
    for x in color:
        if color[x] in frequency_dict:
            frequency_dict[color[x]] += 1
        else:
            frequency_dict[color[x]] = 1
        
    max_color: str = ""
    max_frequency: int = -1

    for y in frequency_dict:
        if frequency_dict[y] > max_frequency:
            max_frequency = frequency_dict[y]
            max_color = y
    return max_color


def count(number: list[str]) -> dict[str, int]:
    """Returns frequency of each key."""
    frequency_dict: dict[str, int]
    frequency_dict = {}

    for x in number:
        if x in frequency_dict:
            frequency_dict[x] += 1
        else:
            frequency_dict[x] = 1
        
    return frequency_dict