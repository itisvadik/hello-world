for n in range(100, 1, -1):
    s = bin(n)[2:]
    s = str(s)
    if n % 2 == 0:
        s += '00'
    else:
        s += '11'
    r = int(s, 2)
    if r < 94:
        print(n)
        break
