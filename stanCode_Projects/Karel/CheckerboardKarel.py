"""
File: CheckerboardKarel.py
Name: Jane
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel put beepers as checkerboard pattern in any world
    way1: different side climb up
    """

    while not facing_north():
        fill_one_line()
        if on_beeper():
            move_to_next()
            if front_is_clear():
                move()
        else:
            move_to_next()


def move_to_next():
    """
    move to next row
    """
    if facing_east():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def fill_one_line():
    """
    fill one row by checkerboard pattern
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


# def main():
#     """
#     Karel put beepers as checkerboard pattern in any world
#     way2: same side climb up
#     """
#     while front_is_clear():
#         fill_one_line()
#         if on_beeper():
#             move_to_next()
#             if front_is_clear():
#                 move()
#         else:
#             move_to_next()
#
#
# def move_to_next():
#     turn_right()
#     if front_is_clear():
#         move()
#         turn_right()
#
#
# def fill_one_line():
#     put_beeper()
#     while front_is_clear():
#         move()
#         if front_is_clear():
#             move()
#             put_beeper()
#
#     back_a1()
#
#
# def back_a1():
#     turn_around()
#     while front_is_clear():
#         move()
#
#
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     for i in range(3):
#         turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)


