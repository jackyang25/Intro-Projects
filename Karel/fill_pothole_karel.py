from karel.stanfordkarel import *

# Author: Jack Yang

"""
File: fill_pothole_karel.py
--------------------------------
When you finish writing the fill_pothole_karel.py file, Karel
should be able to fill the potholes of an arbitrary length
world, with potholes on assorted avenues of the first street.
A more in depth description of the problem can be found in the 
Assignment 1 instructions.  You should make sure that your 
program works for all of the sample worlds listed in the 
instructions for this problem.
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

    turn_left()
    turn_left()


def search_pothole():
    """
    description: allows Karel to look if there is potholes to fill

    pre-condition: Karel's right has tobe clear
    post-condition: Karel turns right if its right is clear
    """

    while facing_east():
        move()
        if right_is_clear():
            turn_right()


def fill_pothole():
    """
    description: allows Karel to fill empty potholes and returns back up without filling it if its already filled

    pre-condition: there has to be an empty pothole for Karel to fill
    post-condition: Karel fills empty pothole
    """

    move()
    if on_beeper():
        u_turn()
        move()
        turn_right()
    else:
        put_beeper()
        while front_is_clear():
            move()
            put_beeper()
        if not front_is_clear():
            u_turn()
            while on_beeper():
                move()
            turn_right()


def get_first_hole():
    """
    description: Karel gets the first hole in AllPotholes1.kwld

    pre-condition: coordinate (1,2) has to be empty for Karel to fill
    post-condition: Karel fills (1,2) on AllPotholes1.kwld
    """

    turn_right()
    move()
    put_beeper()
    u_turn()
    move()
    turn_right()


def main():
    """
    description: allows Karel to fill all the empty potholes in the world

    pre-condition: there has to be empty potholes for Karel to fill
    post-condition: Karel fills all the empty potholes in the world
    """

    if right_is_clear():
        get_first_hole()
    while facing_east():
        search_pothole()
        fill_pothole()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
