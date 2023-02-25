n = int(input('n: '))
max_num = -1
for i in range(n):
    num = int(input('num: '))
    if num > max_num and num % 5 == 0 and not(num % 10 == 0):
        max_num = num
print(max_num)
