from turtle import *

t = Turtle()
size = 30
t.lt(90)

for i in range(3):
    t.fd(10 * size)
    t.rt(120)

t.up()
tracer(5)
for x in range(-2, 30):
    for y in range(-2, 20):
        t.goto(x * size, y * size)
        t.dot(4)

exitonclick()
