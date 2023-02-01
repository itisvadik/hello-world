from turtle import *
t = Turtle()
t.left(90)
t.speed(20)
size = 20

for i in range(4):
    t.forward(12 * size)
    t.rt(90)

for i in range(3):
    t.forward(12 * size)
    t.rt(120)

t.up()
for x in range(13):
    for y in range(13):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()

