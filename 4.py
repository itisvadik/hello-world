N = int(input('введите число в десятеричной системе счисления: '))
x = bin(N)
print(x)
n = x[2:]
print(n)
if '10' in n:
    b = n[2:]
    print(b)
    r = int(str(b), 2)
    print(r)


