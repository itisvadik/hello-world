for i in range(2, 1500):
    n = i
    n = bin(n)[2:-1]
    if n.count('1') % 2 == 0:
        n += '10'
    else:
        n += '01'
    r = int(n, 2)
    print(i, n, r)
    if r >= 2018:
        break


