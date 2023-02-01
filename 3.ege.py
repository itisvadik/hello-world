a = 3 * 125**6 + 2 * 25**9 + 5**12 - 625
count = 0

print(a)
print(a[2:])
print(a[2:].count('0'))

while a:
    n = a % 5
    if not n:
        count += 1
    a //= 5

print(count)
