count = 0
for a in 'РУЧКА':
    for b in 'РУЧКА':
        for c in 'РУЧКА':
            word = a + b + c
            if word.count('К') == 1:
                count += 1
print(count)
