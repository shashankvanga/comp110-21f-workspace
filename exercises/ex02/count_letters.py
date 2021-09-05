"""Counting letters in a string."""

__author__ = "730489843"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

counter: int = 0

index = 0

while index < len(word):
    character = word[index]
    index = index + 1
    if character == letter:
        counter = counter + 1
print("Count: " + str(counter))