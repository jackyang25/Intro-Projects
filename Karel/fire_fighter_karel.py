from karel.stanfordkarel import * 

# Author: Jack Yang

"""
File: fire_fighter_karel.py
--------------------------------
When you finish writing this file, fire_fighter_karel.py should be
able to extinguish the fires in all three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
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


def u_turn():
    """
    description: uses 2 turn_right functions to create a u_turn function to allow Karel to turn around when needed

    pre-condition: none
    post-condition: makes Karel turn 180 degrees
    """

    turn_right()
    turn_right()


def check_for_beeper():
    """
    description: allows Karel to check if there are beepers its proximity and turning when there is a corner

    pre-condition: if its right is clear and if there is a corner
    post-condition: turns right when right is clear and left when there is a corner
    """

    if right_is_clear():
        turn_right()
        move()
    else:
        move()
    if not right_is_clear() and not front_is_clear() and left_is_clear():
        turn_left()


def clear_beeper_line():
    """
    description: allows Karel to pick up beepers depending on its situation

    pre-condition: Karel has to be on a beeper and moves when there is no beeper
    post-condition: Karel collects all the beepers
    """

    while on_beeper() and not right_is_clear() and not left_is_clear():
        pick_beeper()
    if not right_is_clear() and not left_is_clear():
        u_turn()
        move()
    while front_is_clear() and on_beeper():
        pick_beeper()
        while not on_beeper() and not right_is_clear():
            move()
        if not front_is_clear():
            turn_left()


def main():
    """
    description: allows Karel to pick up all the beepers in its world while avoiding obstacles

    pre-condition: none
    post-condition: Karel picks up all the beepers in its world
    """

    check_for_beeper()
    clear_beeper_line()
    move()
    check_for_beeper()
    clear_beeper_line()
    move()
    check_for_beeper()
    clear_beeper_line()
    move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
