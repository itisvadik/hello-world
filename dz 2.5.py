a = int(input('a: '))
b = [int(input('b: ')) for i in range(a)]
s = 0

for i in range(a):
    s += b[i]
if s % 2 == 0:
    print(s)
else:
    print(2 * s)
