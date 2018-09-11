from turtle import *
speed(0)
def draw_square(length, square_color):
    color(square_color)
    for j in range(4):
        forward(length)
        left(90)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()


mainloop()
    