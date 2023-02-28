# 88x4y_9 + 7x44y_11
for x in range(9):
    for y in range(9):
        n = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        print(f'{x=} {y=} {n=} {n%61=}')
        if n % 61 == 0:
            print(n // 61)
