a = int(input('a: '))
b = [int(input('b: ')) for i in range(a)]
s = 0
sm = 0

for i in range(a):
    if b[i] < 0:
        sm += b[i]
    if b[i] > 0:
        s += b[i]
print(s, sm)
