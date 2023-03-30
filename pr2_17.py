with open('17.txt') as f:
    g = f.read()
    a = [int(i) for i in f]
    count = 0
    for i in range(len(g) + 1):
        if (a[i] - a[i + 1]) % 60 == 0 and (a[i] % 15 == 0 or a[i + 1] == 0):
            count += 1
        print(i)
