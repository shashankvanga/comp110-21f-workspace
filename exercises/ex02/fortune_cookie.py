"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730489843"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")

rand_result_1 = "You will live a wonderful life."
rand_result_2 = "A loyal, hardworking and beautiful person will enter your life soon."
rand_result_3 = "You will experience actual success soon."
rand_result_4 = "You will stumble into the happiness of your life"

number = randint(1, 4)

if number == 1:
    print(rand_result_1)
else:
    if number == 2:
        print(rand_result_2)
    else:
        if number == 3:
            print(rand_result_3)
        else:
            print(rand_result_4)   

print("Now, go spread positive vibes!")