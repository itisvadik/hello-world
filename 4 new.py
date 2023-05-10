count = 0
for a in 'ВИНЯ':
    for b in 'ВИШНЯ':
        for c in 'ВИШНЯ':
            for d in 'ВИШНЯ':
                for e in 'ВИШНЯ':
                    for f in 'ВШН':
                        word = a + b + c + d + e + f
                        if word.count('В') <= 1:
                            count += 1

print(count)
