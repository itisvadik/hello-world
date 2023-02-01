from turtle import *
t = Turtle()
t.speed(10)
t.left(90)
size = 30

for i in range(6):
    t.forward(7 * size)
    t.rt(90)
    t.forward(7 * size)
    t.rt(90)

t.up()
for x in range(8):
    for y in range(8):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
