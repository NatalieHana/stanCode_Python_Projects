"""
File: MidpointKarel.py
Name: Jane
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    輪流清空兩側找中點
    """

    start_cln()
    while on_beeper():
        right_off()
        left_off()
    put_beeper()
    # 找到中點放球


def start_cln():
    # 中間放球,兩側是空
    while front_is_clear():
        put_beeper()
        move()
    turn_around()
    while front_is_clear():
        move()
    while on_beeper():
        pick_beeper()
    turn_around()
    if front_is_clear():
        move()


def right_off():
    # 一步步清空右側球
    while on_beeper():
        move()
    turn_around()
    move()
    if on_beeper():
        pick_beeper()
        move()


def left_off():
    # 一步步清空左側球
    while on_beeper():
        move()
    turn_around()
    move()
    if on_beeper():
        pick_beeper()
        move()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
