from turtle import *
t = Turtle()
t.speed(10)
t.left(90)
size = 40

for i in range(5):
    t.forward(9 * size)
    t.rt(120)

t.up()
for x in range(10):
    for y in range(-5, 10):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
