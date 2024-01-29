"""
File: hangman.py
Name: Natalie
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    hangman game player guess word in N_turn
    """

    word = random_word()
    guess = ""  # player guess alphabet
    turn = N_TURNS  # step allowed to guess
    initial = "-" * len(word)

    print("The word looks like: " + initial)
    print("You have " + str(turn) + " wrong guesses left.")

    while True:
        ans = ""
        guess = input("Your guess: ").upper()
        if guess.isalpha() is False:
            print("Illegal format")
        elif len(guess) != 1:
            print("Illegal format")
        elif initial.find(guess) != -1:
            print("You are correct")
            print("The word looks like: " + initial)
            print("You have " + str(turn) + " wrong guesses left.")
        else:
            for i in range(len(word)):
                ch = word[i]
                if ch == guess:
                    ans += guess
                else:
                    ans += initial[i]
            if ans == initial:
                turn -= 1
                print("There is no " + str(guess) + " in the word.")
                print("The word looks like: " + initial)
                print("You have " + str(turn) + " wrong guesses left.")
            else:
                initial = ans
                print("You are correct!")
                print("The word looks like: " + initial)
                print("You have " + str(turn) + " wrong guesses left.")
        if turn == 0:
            print("You are completely hang :(")
            print("The answer is: " + word)
            break
        if initial.find("-") == -1:
            print("You win!!")
            print("The answer is: " + word)
            break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
