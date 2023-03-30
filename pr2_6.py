from turtle import Turtle, tracer, getcanvas, mainloop

t = Turtle()
tracer(5)
size = 30
t.lt(90)
count = 0
t.color('black', 'green')

t.begin_fill()
for i in range(4):
    t.fd(7 * size)
    t.rt(90)
    t.fd(4 * size)
    t.fd(90)
t.end_fill()
t.up()
t.pensize(4)

canvas = getcanvas()
for x in range(-1 * size, 22 * size, size):
    for y in range(-14 * size, 9 * size, size):
        s = canvas.find_overlapping(x, -y, x, -y)
        print(f'{x=} {y=} {s=}')
        if 4 in s:
            t.color('brown')
            count += 1
        elif 5 in s:
            t.color('red')
            count += 1
        else:
            t.color('blue')
        t.goto(x, y)
        t.dot(4)
print(count)
mainloop()

