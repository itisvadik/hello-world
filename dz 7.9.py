x = 100 ** 2023 + 23 * 10 ** 23 + 20 ** 23 + 101
count = 0
while x > 0:
    x % 4
    x //= 9
print(str(x).count('0') + str(x).count('3'))
