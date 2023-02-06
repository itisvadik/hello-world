a = 3
b = [int(input('b: ')) for i in range(a)]
sum = 0

for i in range(a):
    sum += b[i]
print(sum)
