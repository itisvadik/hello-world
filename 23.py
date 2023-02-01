def twenty_three_dex(n):
    if n == 3:
        return 1
    elif n % 3 == 0:
        return twenty_three_dex(n // 3) + twenty_three_dex(n - 3)
    else:
        return 0


print(twenty_three_dex(93))
