# (¬z ≡ y) → ((w ∧ ¬x) ≡ (y ∧ x))
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not z == y) <= ((w and not x) == (y and x))) == 0:
                    print(x, y, z, w)
