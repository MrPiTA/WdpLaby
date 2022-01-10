
# dla zadanej liczby całkowitej w systemie 2 wyświetli jej odpowiednik w systemie dziesiątkowym

n = int(input("Podaj n: "))

suma = 0
licznik = 0

while n > 0:
    cyfra = n%10
    suma += cyfra * 2**licznik
    licznik += 1
    n = (n - cyfra)/10
print(suma)