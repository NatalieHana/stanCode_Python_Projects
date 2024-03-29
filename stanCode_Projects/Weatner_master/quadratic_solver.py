"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Solution for ax^2 + bx + c = 0
	"""
	print("stanCode Quardratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	discriminant = b*b-4*a*c

	if discriminant > 0:
		x = float(-b + math.sqrt(discriminant)) / (2 * a)
		y = float(-b - math.sqrt(discriminant)) / (2 * a)
		print("Two roots: " + str(x) + ", " + str(y))
	elif discriminant == 0:
		x = float(-b + math.sqrt(discriminant)) / (2 * a)
		y = float(-b - math.sqrt(discriminant)) / (2 * a)
		print("One root: " + str(x))
	else:
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
