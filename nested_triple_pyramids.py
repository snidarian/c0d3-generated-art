#!/usr/bin/python3


import turtle as t
import random as r
from hex_color_sets import color_sets

pen = t.Turtle()
pen.speed(0)

color_set = color_sets.chill_blues_super_light

pen.color(r.choice(color_set))

pen.getscreen().bgcolor('black')


def draw_triangle(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(3):
            pen.right(120)
            pen.forward(size)
        # sets up to draw next inner triangle
        pen.right(120)
        pen.penup()
        pen.forward(size * .4)
        pen.pendown()
        pen.color(r.choice(color_set))
        draw_triangle(size-10)



def main(size):
    pen.penup()
    pen.setpos(0, 250)
    pen.pendown()
    draw_triangle(size)





main(500)







t.done()

