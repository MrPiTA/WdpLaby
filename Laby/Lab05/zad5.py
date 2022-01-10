
def print2D(tablica):
    for i in range(len(tablica)):
        print(tablica[i])

n = int(input("n: "))

tablica = [[j for j in range(n)] for i in range(n)]

print(tablica)
print2D(tablica)

# oblicza sume przekątnych tablicy

suma_l = 0
suma_r = 0
suma = 0

for i in range(len(tablica)):
    for l in range(len(tablica)):
        if i == l:
            suma_l += tablica[i][l]
    # druga przekątna
    suma_r += tablica[i][len(tablica)-i-1]

suma = suma_r + suma_l

if n % 2 != 0:
    srodek = n//2
    suma -= tablica[srodek][srodek]

print(suma)
print(suma_l)
print(suma_r)
