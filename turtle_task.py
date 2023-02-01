from turtle import *
t = Turtle()
t.speed(10)
t.left(90)
size = 40


for i in range(5):
    t.forward(5 * size)
    t.rt(60)

t.up()
for x in range(15):
    for y in range(-5, 15):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
