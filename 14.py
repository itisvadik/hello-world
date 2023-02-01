x = 8**2020 + 4**2017 + 26 - 1
count = 0
n = len(str(x))
for i in range(n+1):
    if '1' in str(x):
        count += 1
print(count)
