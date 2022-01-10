
# stworzy liste z wszystimi literami alfabetu

# alphabet = []
# panagram = "The quick brown fox jumps over the lazy dog"
# panagram = panagram.replace(" ", "")
# panagram = panagram.lower()
# panagram = sorted(panagram)
#
# for letter in panagram:
#     if letter not in alphabet:
#         alphabet.append(letter)
# print(alphabet)

def is_panagram(zdanie):
    # lista zawierająca alfabet z nią będziemy porównywać
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # przekonwerowujemy litery zdania na listę, posortowaną i bez duplikatów
    zdanie = zdanie.replace(" ", "")
    zdanie = zdanie.lower()
    zdanie = sorted(zdanie)

    # napis to zdanie po przekonwertowaniu na posortowaną listę, bez duplikatów
    napis = []
    for letter in zdanie:
        if letter not in napis:
            napis.append(letter)

    # sprawdza czy lista napis jest taka sama jak lista alfabet
    if napis == alphabet:
        return "TAK"
    else:
        return "NIE"


print(is_panagram("The quick brown fox jumps over the lazy dog"))



