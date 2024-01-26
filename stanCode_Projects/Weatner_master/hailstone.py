"""
File: hailstone.py
Name: Jane
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = 1  # Sentinel value


def main():
    """
    Hailstone Sequence : from n to 1
    for n is (1) odd: 3n+1 (2) even: n/2
    """
    print("This program computes Hailstone sequences.")
    step = []
    number = int(input("Enter a number"))
    while True:
        step.append(number)  # 將運算數字加到列表中
        if number == EXIT:
            break
        elif number % 2 == 1:
            number = number*3+1
            print(str((number-1)//3) + " is odd, so I make 3n+1: " + str(number))
        elif number % 2 == 0:
            number = number//2
            print(str(number*2) + " is even, so I take half: " + str(number))
    count = len(step)-1  # 計算運算步驟
    print("It took " + str(count) + " steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
