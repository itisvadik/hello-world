a = 3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2 * 4**4 + 1
count = 0
print(a)
print(hex(a))
print(hex(a)[2:])
print(hex(a)[2:].count('0'))

while a:
    n = a % 16
    if not n:
        count += 1
    a //= 16

print(count)
