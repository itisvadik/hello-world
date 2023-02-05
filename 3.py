with open('3.txt') as file:
    a = file.readline()
    s = 0
    for i in range(len(a)):
        if int(a[i]) % 3 == 0:
            s += int(a[i])
            print(s)
