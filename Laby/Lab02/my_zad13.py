
# pętla ma sprawdzić liczby od 1 do 800

# pętla ma sprawdzać każdy naturalny dzielnik oprócz 1 i tej liczby
# pętla pójdzie więc od 2 aż do (liczba//2) + 1

# dla każdego takiego dzielnika ma zostać sprawdzone czy liczba nie dzieli się przez ten dzielnik.
# jak taka liczba nie dzieli się to ma zostać oznaczona np. przez flagę

# dla każdej oznaczonej liczby ma zostać wyprintowana wiadomość
# ,że ta liczba jest liczbą pierwszą




for i in range(1,801):
    flaga = 0
    for j in range(2, (i//2)+1):
        if i%j == 0:
            flaga = 1
    if flaga == 1:
        print(i, "jest liczbą pierwszą!")