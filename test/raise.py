a = float(input())
try:
    b = float(input())
    if (b == 0):
        raise ZeroDivisionError
except ZeroDivisionError as e:
    print('tak terdefinisi')
else:
    c = a / b
    print(c)