d = '2' + '8' * 99 + '2'

while '81' in d or '882' in d or '8883' in d:
    d = d.replace('81', '2', 1)
    d = d.replace('882', '3', 1)
    d = d.replace('8883', '1', 1)

print(d)
