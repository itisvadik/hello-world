count = 0
with open('3.txt') as file:
    b = [int(i) for i in file]
    if b[i] % 2 != 0:
        count += 1
