from turtle import *
t = Turtle()
t.speed(10)
t.left(90)
size = 30

for i in range(8):
    t.forward(6 * size)
    t.rt(120)

t.up()
for x in range(7):
    for y in range(7):
        t.goto(x * size, y * size)
        t.dot(3)

exitonclick()
