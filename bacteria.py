#!/usr/bin/python3

# My representation of recursive bacteria image generation

import turtle
import math
import random

pen = turtle.Turtle()


pen_colors_list = ['red', 'green', 'blue', 'yellow', 'orange', 'teal']

pen.getscreen().bgcolor('#9f8c76')
pen.speed(0)

# set random positon and produce bacterial shapes
def produce_bacterium(size, x_cord, y_cord, pen_color) -> None:
    pen.color(pen_color)
    pen.up()
    pen.setpos(x_cord, y_cord)
    pen.left(random.randint(0, 90))
    pen.down()
    pen.forward(size)
    for _ in range(10):
        pen.right(18)
        pen.forward(size/10)
    pen.forward(size)
    for _ in range(10):
        pen.right(18)
        pen.forward(size/10)
    pen.begin_fill()
    




for _ in range(1000):
    produce_bacterium(random.randint(1,12), random.randint(-300,600), random.randint(-300,600), random.choice(pen_colors_list))




    
turtle.done()










