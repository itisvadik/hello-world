count = 0
for i in range(10000, 100000 + 1):
    if i % 3 == 0 and not(i % 9 == 0):
        count += 1
        print(i)
print(count)
