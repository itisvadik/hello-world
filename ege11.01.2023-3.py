
n = 24

if n > 0 and n % 2 == 0:
    n = n / 2
    print(n)
else:
    if n // 2 != 0:
        n = 1 + (n - 1)
        print(n)

