count = 0
for a in 'СВЕТА':
    for b in 'СВЕТА':
        for c in 'СВЕТА':
            for x in 'СВЕТА':
                for y in 'СВЕТА':
                    word = a + b + c + x + y
                    if word.count('С') == 1 \
                        and word.count('В') == 1 \
                        and word.count('Е') == 1 \
                        and word.count('Т') == 1 \
                        and word.count('А') == 1 \
                        and word.index('Е') - word.index('А') != 1 \
                        and word.index('А') - word.index('Е') != 1:
                            count += 1
print(count)
