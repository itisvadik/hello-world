# (x & 29 ≠ 0) → ((x & 17 = 0) → (x & А ≠ 0))

for A in range(0, 100):
    for x in range(1, 10000):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))) == 0:
            break
    else:
        print(A)
