
def potegowanie_bez_potegowania(a,b):
    """zad 7"""
    if b == 1:
        return a
    else:
        return a * potegowanie_bez_potegowania(a,b-1)


def nwd(a,b):
    """zad 8"""
    if a > 0 and b > 0:
        if a == b:
            return a
        elif a > b:
            a = a - b
            return nwd(a,b)
        else:
            b = b - a
            return nwd(a,b)
    else:
        return -1


def suma_cyfr_liczby(n):
    """zad 9"""
    if n >= 1:
        cyfra = n % 10
        return cyfra + suma_cyfr_liczby(((n - (cyfra))/10))
    else:
        return 0



print(suma_cyfr_liczby(129))

# print(nwd(2,10))
# print(potegowanie_bez_potegowania(10,10))