from turtle import Turtle, exitonclick, tracer, getcanvas

t = Turtle()
tracer(5)
t.lt(90)
size = 50
count = 0

t.begin_fill()
t.rt(90)
for i in range(3):
    t.fd(8 * size)
    t.rt(120)
t.end_fill()
t.up()
t.color('blue')
t.pensize(4)

canvas = getcanvas()
for x in range(-2 * size, 11 * size, size):
    for y in range(-9 * size, 3 * size, size):
        s = canvas.find_overlapping(x, -y, x, -y)
        print(f'{x=} {y=} {s=}')
        if 4 in s:
            t.color('brown')
        elif 5 in s:
            t.color('red')
            count += 1
        else:
            t.color('blue')
        t.goto(x, y)
        t.dot(4)

print(count)
exitonclick()







