from turtle import *
t = Turtle()
t.left(90)
t.speed(20)
size = 30

for i in range(5):
    t.forward(7 * 30)
    t.rt(90)
    t.forward(4 * size)
    t.rt(90)

t.up()
for x in range(6):
    for y in range(13):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()

