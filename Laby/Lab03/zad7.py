
# znajdzie ilość znaków sumy a+b

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

suma = a+b
cyfra = 0
licznik = 0

while suma > 0:
    cyfra = suma%10
    # print("cyfra:", cyfra)
    licznik += 1
    suma = (suma - cyfra)/10
print("Ilość znaków sumy:", licznik)


