"""
https://edabit.com/challenge/3ZtykTsx3GSoPHyBb

There are three towers. The objective of the game is to move all
the disks over to tower #3, but you can't place a larger disk onto
a smaller disk.To play the game or learn more about the Tower of Hanoi,
check the Resources tab.


Create a function that takes a number discs as an argument and returns
the minimum amount of steps needed to complete the game.

Notes
    # The amount of discs is always a positive integer.
    # 1 disc can be changed per move.
"""


def tower_hanoi(discs):
    # The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks (wikipedia)
    return pow(2, discs) - 1

