start = int('10000', base=8)
stop = int('0o77777', base=8)
count = 0

for number in range(start, stop+1):
    number = oct(number)[2:]
    if len(number) == len(set(number)):
        flag = False
        for i in range(len(number)-1):
            if int(number[i]) % 2 == int(number[i+1]) % 2:
                flag = True
                break
        if not flag:
            count += 1
print(count)
