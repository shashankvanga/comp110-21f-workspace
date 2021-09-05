"""Repeating a beat in a loop."""

__author__ = "730489843"


beat: str = input("What beat do you want to repeat? ")
repetition: int = int(input("How many times do you want to repeat your beat? "))
counter: int = 0

if counter <= 0: 
    print("No beat...")
else:

    beat_string = ""

    while counter < repetition - 1:
        beat_string = beat_string + beat + " " 
        counter = counter + 1
        
    beat_string = beat_string + beat

    print(beat_string)

