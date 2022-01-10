
x = int(input("liczba: "))
cyfry = len(str(x))

suma = 0

for i in range(cyfry):
    i += 1
    suma += (((x%(10**i)) - (x%(10**(i-1)))) / (10**(i-1)))
print(suma)
print(cyfry)

# j = x%10
# d = ((x%100) - x%10)/10
# s = ((x%1000) - x%100)/100
#
#
# print(s, d, j)



# nie działa

# def suma_cyfr_rekurencyjnie(x):
#     liczba = str(x)
#     cyfry = len(liczba)
#     y = liczba[1:]
#     if cyfry == 0:
#         return 0
#     else:
#         return (((x%(10**cyfry)) - (x%(10**(cyfry-1)))) / (10**(cyfry-1))) + suma_cyfr_rekurencyjnie(int(y))
#
# print(suma_cyfr_rekurencyjnie(123))





