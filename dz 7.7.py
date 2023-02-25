x = 278 * 17 ** 44 + 23 * 14 ** 2023 - 100 * 101 ** 44 + 1
count = 0
while x > 0:
    if (x % 9) % 4 != 0:
        count = count + x % 9
    x //= 9
print(count)
