with open('2.txt') as file:
    a = file.readline()
    count = 0
    for i in range(len(a)):
        if int(a[i]) % 2 == 0:
            count += 1
print(count)
