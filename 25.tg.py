# mask 2?1*67 // 159
a = '2'
c = '1'
e = '67'
numbers = []
for b in '0123456789':
    number = int(a + b + c + e)
    if number % 159 == 0:
        numbers.append((number, number // 159))
    for d in range(100):
        number = int(a + b + c + str(d) + e)
        if number % 159 == 0:
            numbers.append((number, number // 159))
for item in sorted(numbers):
    print(*item)
