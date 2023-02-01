count = 0
with open('inf_22_10_20_24.17.txt') as file:
    for line in file:
        if line.count('E') < line.count('A'):
            count += 1

print(count)
