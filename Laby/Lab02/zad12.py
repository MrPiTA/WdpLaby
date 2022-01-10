
n = int(input("liczba: "))

sum_kwad = 0

for i in range(n):
    sum_kwad += ((n-i)**3)
print(sum_kwad)