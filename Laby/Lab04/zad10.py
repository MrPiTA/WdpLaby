
liczby = input("liczby: ").split(",")

for liczba in liczby[:]:
    liczba_int = int(liczba)
    liczby.remove(liczba)
    liczby.append(liczba_int)
print(liczby)

#

for liczba in liczby:
    if liczba % 2 == 1:
        print(liczba)