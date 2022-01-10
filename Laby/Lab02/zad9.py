
x = int(input("liczba: "))

silnia = 1

for i in range(x):
    silnia *= (x - i)

print(silnia)