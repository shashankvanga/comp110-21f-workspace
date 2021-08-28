"""Uses the user's input to demonstrate how relational operators work"""

__author__ = "730489843"

lhs: str = input("Left-hand side: ")
rhs: str = input("Right-hand side: ")

converted_lhs = int(lhs)
converted_rhs = int(rhs)

print(lhs + " < " + rhs + " is " + str(converted_lhs < converted_rhs))
print(lhs + " >= " + rhs + " is " + str(converted_lhs >= converted_rhs))
print(lhs + " == " + rhs + " is " + str(converted_lhs == converted_rhs))
print(lhs + " != " + rhs + " is " + str(converted_lhs != converted_rhs))
