
# proste zamienianie w przybliżeniu ,że każdy rok ma 365 dni

def lata_minuty(n):
    minuty = n * 365 * 24 * 60
    return minuty


def lata_minuty2(n,m):

    def ilosc_przestepnych(n, m):
        liczba = 0  # liczba lat przestępnych
        for rok in lata:
            if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
                liczba += 1
        return liczba

    if 0 < n < m:
        lata = [i for i in range(n, m)]
        minuty = (((len(lata) - ilosc_przestepnych(n, m)) * 365) + ((ilosc_przestepnych(n, m) * 366) * 24 * 60))
        return minuty


print(lata_minuty2(2000,2001))


# niedokończone i milion errorów