A = [2, 11, -9, 8, 4, 3, -3, 8, -5, -10]
s = 1
for i in range(10):
    if A[i] <= A[2]//3:
        s = s * i
print(s)
