
# liczba pierwsza to taka która nie jest podzielna przez żaden swój dzielnik
# oprócz 1 i samej siebie

# 1) ta pętla sprawdza dla każdej liczby od 1 do 801 czy, jest podzielna przez każdy z swoich dzielników od 2 do największego
# który, nie jest tą liczbą.
# 2) Największym takim dzielnikiem jest oczywiście ten który mnożąc dwa razy tą liczbę da nią samą
# 4,5 * 2 = 9 -> 4,5 to największy jej dzielnik
# trzeba podzielić liczbę przez 2, żeby go dostać.
# Dzielniki jednak muszą być naturalne, więc dzielimy floorem, by dostać największy naturalny dzielnik
# dodajemy jeden, oczywiście ,żeby został uwzględniony w iteracji pętli, w której zmienną "i" są kolejne dzielniki
# przez to ,że zaczynamy sprawdzać od 2 to dla 0 i 1 nawet nie ruszy ta pętla


for i in range(1,801): # 1)
  flaga = 0
  for j in range(2,((i//2)+1)): # 2)
    if i%j == 0: # sprawdza czy liczba jest podzielna przez dzielnik, jak jest zostanie oznaczona przez zmianę flagi
      flaga = 1 # zmienia się jej tu od niej flaga, od której zależy czy zostanie wyprintowana wiadomość
  if flaga == 0: # jak flaga się nie zmieni to znaczy ,że nie jest podzielna przez żaden z tych dzielników, a co za tym idzie jest pierwsza !
    print(i," jest pierwsza")



