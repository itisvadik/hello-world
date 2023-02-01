count = 0
with open('inf_26_04_21_24.24.txt') as file:
    for line in file:
        if line.count('A') < 35:

            count += 1

print(count)
