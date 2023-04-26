for i in range(1, 100):
    n = bin(i)[2:]
    if int(n) % 2 == 0:
        z = '1' + str(n) + '0'
    else:
        z = '11' + str(n) + '11'
    r = int(z, 2)
    if r > 52:
        print(int(n, 2))
        break
