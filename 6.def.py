from turtle import Turtle, mainloop, tracer, getcanvas

t = Turtle()
tracer(1)
t.lt(90)
size = 30
t.color('black', 'green')

t.begin_fill()
for i in range(2):
    t.fd(5 * size)
    t.rt(90)
    t.fd(10 * size)
    t.rt(90)
t.end_fill()
t.up()
t.color('blue')
t.pensize(4)

canvas = getcanvas()
for x in range(1, 5):
    for y in range(1, 4):
        t.dot(4)
        t.goto(x * size, y * size)


mainloop()
