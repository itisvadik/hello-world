a = '7' * 85
while '777' in a or '333' in a:
    if '333' in a:
        a = a.replace('333', '7', 1)
    if '777' in a:
        a = a.replace('777', '3', 1)

print(a)
