num = []
count = 0
max_pare = 0

with open('17.txt') as file:
    for number in file:
        num.append(int(number))
for i in range(len(num) - 1):
    if num[i] % 3 == 0 or num[i+1] % 3 == 0:
        count += 1
        if num[i] + num[i+1] > max_pare:
            max_pare = num[i] + num[i+1]
        # max_pare = max(max_pare, num[i] + num[i+1])
print(count, max_pare)
