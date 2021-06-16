#!/usr/bin/python3


import turtle as t


pen = t.Turtle()
pen.color('red')
pen.getscreen().bgcolor('blue')
pen.speed(0)


color_set = ['red', 'yellow', 'orange', 'green', 'purple', 'cyan', 'white', 'maroon', 'pink', 'black']

pen.right(180)

def draw_angled_lines(size, index) -> None:
    if size < 3:
        return
    else:
        for _ in range(4):
            pen.forward(size)
            pen.left(90)
            pen.forward(size)
            draw_angled_lines(size/2, (index +1))
            pen.color(color_set[index])
            pen.backward(size/2)
            pen.color(color_set[index -1])
            pen.backward(size/2)
            pen.right(90)
            pen.backward(size)
            pen.right(90)


# call with '1' index so the first [-1 index] recursive call finds a legitimate value in the color_set list
draw_angled_lines(100, 1)



t.done()





