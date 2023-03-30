count = 0
for a in 'АВХ':
    for b in 'АВХ':
        for c in 'АВХ':
            for d in 'АВХ':
                for x in 'АВХ':
                    for y in 'АВХ':
                        word = a + b + c + d + x + y
                        if word.count('Х') == 1 and word.count('А') == 1:
                            count += 1
print(count)