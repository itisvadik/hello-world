import itertools


s = 'ПРЕПАРАТ'
p = itertools.combinations(s, 8)

for i in p:
    print(i)
