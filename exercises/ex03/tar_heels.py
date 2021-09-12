"""An exercise in remainders and boolean logic."""

__author__ = "730489843"


number: int = int(input("Enter an int: "))

divisble_by_2 = number % 2 == 0
divisble_by_7 = number % 7 == 0
    
if divisble_by_2:
    if divisble_by_7:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if divisble_by_7:
        print("HEELS")
    else:
        print("CAROLINA")    