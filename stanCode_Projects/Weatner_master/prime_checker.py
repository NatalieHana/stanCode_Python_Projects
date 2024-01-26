"""
File: prime_checker.py
Name: Jane
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100  # Sentinel value


def main():
	"""
	prime checker by for i in range(x, y)
	"""
	print("Welcome to the prime checker!")
	while True:
		number = int(input("n: "))
		n = 0
		if number == EXIT:
			break
		else:
			for i in range(2, number):
				if number % i == 0:
					n += 1
			if n > 0:
				print(str(number) + " is not a prime number.")
			else:
				print(str(number) + " is a prime number")
	print("Have a good one!")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
