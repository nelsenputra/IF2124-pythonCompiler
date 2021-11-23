A = 10
B = int(input("B = "))
if (((A <= 9) or (A > 10)) and not (A == 10)):
    print("A != 10")
elif (A is B):
    print("A = B")
else: # A != B
    print("A != B")