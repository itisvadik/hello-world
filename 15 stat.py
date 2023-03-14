for A in range(1, 100):
    flag = True
    for x in range(1, 1000):
        if (((x&35 != 0) or (x&22 != 0)) <= ((x&15 == 0) <= (x&A != 0))) == 1:
            flag = False

        if flag:
            print(f'{A=} {x=}')
