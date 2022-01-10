a = int(input("a: "))
b = int(input("b: "))

x = 1

if a == 0 and b != 0:
    if b != 0:
        print("Funkcja nie ma miejsc zerowych!")
elif a != 0 and b == 0:
    x = 0
    print(x)
elif a == 0 and b == 0:
    print("nieskończenie miejsc zerowych")
else:
    x = -b / a
    print(x)