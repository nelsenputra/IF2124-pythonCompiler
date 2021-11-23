def kali(x, y):
    """
    me-return hasil dari x dikali y
    """
    hasil = x * y
    return hasil
for i in range(1, 11, 2):
    if (i == 5):
        continue
    print(i, end=" ")
print()
i = 1
while (i < 128):
    if (i == 64):
        break
    print(i, end=" ")
    i *= 2