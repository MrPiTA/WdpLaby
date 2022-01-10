
# a = 999
#
# len = len(str(a))
#
#
# pierw_miejsce = a // 10**(len-1)
# a = a - (pierw_miejsce*(10**(len-1)))
# drugie_miejsce = a // 10**(len-2)
# a = a - (drugie_miejsce*(10**(len-2)))
# trzecie_miejsce = a // 10**(len-3)
#
# print(pierw_miejsce, drugie_miejsce, trzecie_miejsce)

# ta metoda faktycznie lepsza

x = 1234

j = x%10
d = ((x%100) - j) / 10
s = (x%1000 - x%100) / 100

print(s, d, j)
