evens = '0246'
odds = '135'
count = 0

for a in '123456':
    for b in '0123456':
        for c in '0123456':
            for d in '0123456':
                for e in '0123456':
                    for f in '0123456':
                        number = a + b + c + d + e + f
                        if number.count('6') == 1:
                            if a in evens and c in evens and e in evens \
                                    and b in odds and d in odds and f in odds:
                                count += 1
                            elif a in odds and c in odds and e in odds \
                                    and b in evens and d in evens and f in evens:
                                count += 1
print(count)
