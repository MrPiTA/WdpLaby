a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a != 0:
    delta = b**2 + (-4*a*c)
    if delta < 0:
        print("brak miejsc zerowych w R")
    if delta == 0:
        x = (-b)/(2*a)
        print(x)
    else:
        pierw_delta = delta**(1/2)
        x_1 = (-b-(pierw_delta))/(2*a)
        x_2 = (-b+(pierw_delta))/(2*a)
        print("Pierwiastki to:", x_1, "i", x_2)
else:
    print("Wspólczynnik a nie może być ujemny")



