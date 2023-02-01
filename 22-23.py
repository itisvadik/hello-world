from turtle import *
t = Turtle()
t.left(90)
size = 30

for i in range(4):
    t.forward(6 * size)
    t.right(150)
    t.forward(6 * size)
    t.right(30)

t.up()
for x in range(-1, 10):
    for y in range(-6, 8):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
