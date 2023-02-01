from turtle import *
t = Turtle()
t.speed(10)
t.left(90)
size = 40

for i in range(4):
    t.forward(6 * size)
    t.rt(150)
    t.forward(6 * size)
    t.rt(30 * size)

t.up()
for x in range(5):
    for y in range(-6, 8):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
