for i in range(1, 100):
    n = i
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n += '00'
    else:
        n += '10'
    r = int(n, base=2)
    print(i, r)
    if r >= 85:
        break
