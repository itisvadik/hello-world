from turtle import *
t = Turtle()
t.left(90)
size = 20

for i in range(6):
    t.forward(10 * size)
    t.right(60)

t.up()
for x in range(-1, 18):
    for y in range(-6, 18):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
