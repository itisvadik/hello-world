for n in range(4, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-3] + s[-2] + s[-1]
    else:
        s += bin((n % 3) * 3)[2:]

    r = int(s, 2)
    if r >= 76:
        print(f'{n=} {s=} {r=}')
        break
