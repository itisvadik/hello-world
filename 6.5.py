from turtle import *
t = Turtle()
t.speed(10)
t.left(90)
size = 20

for i in range(6):
    t.forward(10 * size)
    t.rt(60)

t.up()
for x in range(20):
    for y in range(-7, 17):
        t.goto(x * size, y * size)
        t.dot(4)


exitonclick()


