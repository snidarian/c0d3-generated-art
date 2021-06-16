#!/usr/bin/python3


import turtle as t


pen = t.Turtle()
pen.speed(0)
pen.color('red')
pen.getscreen().bgcolor('blue')


color_set = []

def draw_pentagon(size) -> None:
    if size < 1:
        return
    else:
        for _ in range(5):
            pen.forward(size)
            pen.right(72)
        pen.left(10)
        draw_pentagon(size -3)



def main(size):
    draw_pentagon(size)





main(200)







t.done()

