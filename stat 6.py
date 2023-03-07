from turtle import Turtle, exitonclick, tracer, getcanvas

t = Turtle()
tracer(3)
t.lt(90)
size = 30
t.color('black', 'green')
count = 0

t.begin_fill()
for i in range(3):
    t.fd(7 * size)
    t.rt(90)
t.fd(10 * size)
for i in range(3):
    t.lt(90)
    t.fd(6 * size)
t.end_fill()
t.up()
t.color('blue')
t.pensize(4)

canvas = getcanvas()
for x in range(-7 * size, 10 * size, size):
    for y in range(-7 * size, 10 * size, size):
        s = canvas.find_overlapping(x, -y, x, -y)
        print(f'{x=} {y=} {s=}')
        if 4 in s:
            t.color('brown')
            count += 1
        elif 5 in s:
            t.color('red')
        else:
            t.color('blue')
        t.goto(x, y)
        t.dot(4)

print(f'{count = }')
exitonclick()
