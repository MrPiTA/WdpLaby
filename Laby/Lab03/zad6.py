

# znajdzie ilość dzielników podanej liczby n

n = int(input("Podaj n: "))

dzielnik = 1
licznik = 0

while dzielnik <= n:
    if n%dzielnik == 0:
        print(dzielnik, end=",")
        licznik += 1
    dzielnik += 1

print("\r")
print("Dzielników jest:", licznik)