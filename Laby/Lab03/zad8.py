
# dla podanej liczby n znajdzie liczbę m, która 1+2+3...+m <= n

n = int(input("Podaj n: "))

m = 1
suma = 0


while suma <= n:
    m += 1
    suma += m
m -= 1
print(m)