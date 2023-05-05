from karel.stanfordkarel import *

# Author: Jack Yang

"""
File: collect_newspaper_karel.py
--------------------------------
At present, the collect_newspaper_karel.py file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up and 
drop off the newspaper (represented by a beeper, of course), and 
then return to the initial position in the upper left corner of 
the house.
"""


def turn_right():
    """
    description: uses 3 turn_left functions to create a turn_right function for efficiency

    pre-condition: none
    post-condition: makes Karel turn right
    """

    turn_left()
    turn_left()
    turn_left()


def retrieve_beeper():
    """
    description: allows Karel to retrieve beeper (newspaper) from outside

    pre-condition: none
    post-condition: Karel picks up beeper outside
    """

    while front_is_clear():
        move()
    if not front_is_clear():
        turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    pick_beeper()


def bring_beeper_inside():
    """
    description: Allows Karel to place beeper (newspaper) on (4,2) and return back to its original

    pre-condition: none
    post-condition: Karel places beeper (newspaper) inside the box and returns back to its starting point
    """

    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    move()
    move()
    turn_right()


def main():
    """
    description:

    pre-condition:
    post-condition:
    """
    retrieve_beeper()
    bring_beeper_inside()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
