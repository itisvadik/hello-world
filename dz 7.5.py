x = 2740 * 5 ** 47 - 74 * 15 * 3 ** 15 + 17 ** 8740 + 478 * 1724 ** 457 + 2023
count = 0
while x > 0:
    if x % 7 == 0:
        count += 1
    x //= 7
print(count)
