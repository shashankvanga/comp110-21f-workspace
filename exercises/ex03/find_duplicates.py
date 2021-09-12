"""Finding duplicate letters in a word."""

__author__ = "730489843"


word: str = input("Enter a word: ")

duplicate: bool = False

index: int = 0
while index < len(word):
    character = word[index]
    z: int = index + 1
    while z < len(word):
        character_2 = word[z]
        if character_2 == character:
            duplicate = True
        z = z + 1
    index = index + 1
print("Found duplicate: " + str(duplicate))