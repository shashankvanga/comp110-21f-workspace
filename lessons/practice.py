"""Practice with if-then-else statements - 09/07"""
choice: int = int(input("Enter a number: "))


# Implement the logic to print
# A when < 25
# B when >= 25 and < 50
# C when > 75
# D when >= 50 and <= 75

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")