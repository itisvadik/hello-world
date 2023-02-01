for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n += '00'
    else:
        n += '10'
    r = int(n, 2)

    print(i, n, n.count('1'), r)
    if r >= 43:
        break
