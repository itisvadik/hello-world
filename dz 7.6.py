x = 278 * 17 ** 44 + 23 * 14 ** 2023 - 100 * 101 ** 44 + 1
count = 0
while x > 0:
    if (x % 17) % 5 == 0:
        count += 1
    x //= 17
print(count)
