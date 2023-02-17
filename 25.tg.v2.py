for number in range(159, 10 ** 7 + 1, 159):
    n = str(number)
    if n[0] == '2' and n[2] == '1' and n[-2:] == '67':
        print(number, number // 159)
