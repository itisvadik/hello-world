for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if r > 43:
        print(r)
        break
