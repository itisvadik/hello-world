count = 0

for a in 'АНДРЕ':
    for b in 'АНДРЕЙ':
        for c in 'АНДРЕЙ':
            for d in 'АНДРЕЙ':
                word = a + b + c + d
                if 'А' in word or 'Е' in word:
                    count += 1

print(count)
