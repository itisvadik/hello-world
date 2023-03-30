count = 0
for a in 'НАСТЯ':
    for b in 'НАСТЯ':
        for c in 'НАСТЯ':
            for v in 'НАСТЯ':
                for w in 'НАСТЯ':
                    for y in 'НАСТЯ':
                        word = a + b + c + v + w + y
                        if word.count('А') == 1 and word.count('Я') == 1 \
                            or word.count('А') == 0 and word.count('Я') == 1 \
                            or word.count('А') == 1 and word.count('Я') == 0 \
                            or word.count('А') == 0 and word.count('Я') == 0:
                            count += 1
print(count)
