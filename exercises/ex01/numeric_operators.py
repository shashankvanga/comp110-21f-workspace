"""Uses the user's input to demostrate how numerical operators work."""

__author__ = "730489843"

lhs: str = input("Left-hand side: ")
rhs: str = input("Right-hand side: ")

converted_lhs = int(lhs)
converted_rhs = int(rhs)

operator_one = (converted_lhs ** converted_rhs)
converted_operator_one = str(operator_one)
print(lhs + " ** " + rhs + " is " + converted_operator_one)

operator_two = (converted_lhs / converted_rhs)
converted_operator_two = str(operator_two)
print(lhs + " / " + rhs + " is " + converted_operator_two)

operator_three = (converted_lhs // converted_rhs)
converted_operator_three = str(operator_three)
print(lhs + " // " + rhs + " is " + converted_operator_three)

operator_four = (converted_lhs % converted_rhs)
converted_operator_four = str(operator_four)
print(lhs + " % " + rhs + " is " + converted_operator_four)