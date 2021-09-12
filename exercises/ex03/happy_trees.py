"""Drawing forests in a loop."""

__author__ = "730489843"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

if depth > 0:
    row: int = 1
    tree_string: str = TREE
    while row <= depth:
        print(tree_string)
        row = row + 1
        tree_string = tree_string + TREE