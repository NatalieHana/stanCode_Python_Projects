"""
File: StoneMasonKarel.py
Name: Jane
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel fill all pillars in any world, facing East at final pillar
    """
    while front_is_clear():
        up()
        down()
        cross()
    up()
    down()


def up():
    # go up pillar
    turn_left()
    while front_is_clear():
        move()


def down():
    # go down pillar and put beeper
    turn_around()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def cross():
    # cross to the next pillar
    for i in range(4):
        move()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
