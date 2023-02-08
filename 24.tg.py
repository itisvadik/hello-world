with open('24.txt') as file:
    line = file.readline()

radiants = [
    'BAB',
    'BAC',
    'CAB',
    'CAC',
]
flag = 0
max_count = count = 0
for i in range(len(line)):
    if flag > 0:
        flag -= 1
        continue
    elif line[i:i+3] in radiants:
        count += 3
        flag = 2
    else:
        max_count = max(count, max_count)
        count = 0

print(max_count)
