# 8x78y_13 + 79xy7_18
for x in range(13):
    for y in range(13):
        t = int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 13)
        if t % 9 == 0:
            t = t // 9
            print()
