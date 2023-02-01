S = '1' * 39 + '2' * 39

while '111' in S:
    S = S.replace('111', '2', 1)
    S = S.replace('222', '1', 1)

print(S)
