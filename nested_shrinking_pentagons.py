#!/usr/bin/python3


import turtle as t
import random as r
from hex_color_sets import color_sets

pen = t.Turtle()
pen.speed(0)
pen.color('red')

#color_set = ['#292a2c', '#6a1611', '#bc342d', '#85201b', '#bababb']
color_set = color_sets.HHteal


pen.getscreen().bgcolor('black')


def draw_pentagon(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(5):
            pen.forward(size)
            pen.right(72)
        # sets up to create next inner pentagon
        pen.right(72)
        pen.penup()
        pen.forward(5)
        pen.left(72)
        pen.pendown()
        pen.color(r.choice(color_set))
        draw_pentagon(size-10)



def main(size):
    pen.penup()
    pen.setpos(-200, 350)
    pen.pendown()
    draw_pentagon(size)





main(500)







t.done()

