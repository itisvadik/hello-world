from turtle import *
t = Turtle()
t.left(90)
t.speed(30)
size = 40

for i in range(4):
    t.forward(7 * size)
    t.right(90)
    t.forward(8 * size)
    t.right(90)
t.up()
for x in range(0, 9):
    for y in range(0, 8):
        t.goto(x * size, y * size)
        t.dot(4)
exitonclick()
