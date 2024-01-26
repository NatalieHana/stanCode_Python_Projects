"""
File: CollectNewspaperKarel.py
Name: Jane
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel take back the newspaper
    """
    go_outside()
    back_home()


def go_outside():
    """
    Pre-condition: at Street 4, Avenue 3
    Post-condition: at Street 3, Avenue 6
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def back_home():
    """
    Pre-condition: at Street 3, Avenue 6
    Post-condition: at Street 4, Avenue 3
    """
    pick_beeper()
    turn_around()
    # facing West
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
