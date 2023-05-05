from karel.stanfordkarel import *

# Author: Jack Yang

"""
File: construction_karel.py
--------------------------------
At present, the construction_karel.py file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to inspect the street corners in front of 
its starting position, and build a building (a vertical structure
that is 3 beepers tall) in each avenue that has been marked 
with a beeper, as described in the Assignment 1 instructions. Karel 
should end on the 5th avenue, facing east. 
"""


def u_turn():
    """
    description: uses 2 turn_left functions to create a u_turn function for efficiency

    pre-condition: none
    post-condition: makes Karel do a u_turn
    """

    turn_left()
    turn_left()


def double_move():
    """
    description: allows Karel to double move

    pre-condition: none
    post-condition: Karel performs a double move
    """

    move()
    move()


def beeper_checker():
    """
    description: Karel checks for beeper (incomplete building) where it is standing

    pre-condition: there must be a beeper where Karel is standing
    post-condition: Karel builds a 3-beeper tall building
    """

    if on_beeper():
        turn_left()
        move()
        put_beeper()
        move()
        put_beeper()
        u_turn()
        move()
        move()
        turn_left()
        move()


def not_on_beeper_checker():
    """
    description: Karel checks for empty spaces and if there are, it moves an extra space

    pre-condition: there has to be an empty beeper where Karel is standing
    post-condition: Karel moves once
    """
    if not on_beeper():
        move()


def main():
    """
    description: allows Karel to construct incomplete buildings and end on (5,1)

    pre-condition:
    post-condition: if there are incomplete buildings, Karel finishes constructing them. Even if there are no buildings,
    Karel goes straight to (5,1)
    """
    move()
    not_on_beeper_checker()
    beeper_checker()
    move()
    not_on_beeper_checker()
    beeper_checker()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
