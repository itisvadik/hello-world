n_ = 1
while True:
    r = bin(n_)[2:]
    d = sum(r) % 2
    for i in range(2):
        r += str(d)
    n = int(r, 2)
    if n > 43:
        print(n)
        break
