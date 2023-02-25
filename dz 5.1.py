def F(x, y):
    if (x * y) % 2 == 0:
        if (x * y) % 6 == 0:
            return 1
    else:
        return 0
print(F(6, 22))
