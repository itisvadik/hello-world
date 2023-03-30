# yAAx_12 + x02y_14
for x in '123456789AB':
    for y in '123456789AB':
        for A in '123456789AB':
            t = int(f'{y}{A}{A}{x}', 12) + int(f'{x}02{y}', 14)
            if t % 80 == 0:
                t = t // 80
                print(t)
