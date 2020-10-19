#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
from turtle import pendown, penup, setpos, back, forward, left, right

from ch6 import histogram

MAX_DEPTH = 5
BRANCH_LENGTH = 100
SHRINK_FACTOR = 0.8
TURN_ANGLE = 20  # degres


# TODO: Définissez vos fonction ici
def ellipse(masse_volumique: float, a: float=1, b: float=2, c: float=3) -> tuple:
    volume = 4 / 3 * pi * a * b * c
    mass = volume * masse_volumique

    return volume, mass 

def sort(sequence: str) -> tuple:
    return sorted(histogram(sequence).items(), key=lambda x: x[1])[-1]
    

def draw_trunk() -> None:
    left(90)  # Make the tree "upright"
    penup()
    setpos(x=0, y=-200)
    pendown()
    forward(BRANCH_LENGTH)


def draw_left(depth: int, distance: float) -> None:
    left(TURN_ANGLE)
    forward(distance * SHRINK_FACTOR)

    draw_tree(depth + 1)

    back(distance * SHRINK_FACTOR)
    right(TURN_ANGLE)    

def draw_right(depth: int, distance: float) -> None:
    right(TURN_ANGLE)
    forward(distance * SHRINK_FACTOR)

    draw_tree(depth + 1)

    back(distance * SHRINK_FACTOR)
    left(TURN_ANGLE) 

def draw_tree(depth: int) -> None:
    distance = BRANCH_LENGTH * SHRINK_FACTOR ** depth

    if depth <= MAX_DEPTH:
        draw_left(depth, distance)
        draw_right(depth, distance)

def fibonnaci(n: int) -> int:
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # else:
    #     return fibonnaci(n - 1) + fibonnaci(n - 2)

    return n if n in [0, 1] else fibonnaci(n - 1) + fibonnaci(n - 2)  
    
def main():
    # print(sort("nyaaaan cat"))
    draw_trunk()
    draw_tree(0)

    # input()

    # print(fibonnaci(0))
    # print(fibonnaci(1))
    # print(fibonnaci(3))
    # print(fibonnaci(7))
if __name__ == '__main__':
    #TODO: Appelez vos fonctions ici
    
    main()