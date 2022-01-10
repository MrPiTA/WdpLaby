
# zadanie 8

samochody = {
    "mój": {"marka": None, "model": None, "rok_produkcji": None},
    "kizo": {1: {"marka": "Mercedes", "model": "AMG", "rok_produkcji": 2020}, 2: {"marka": "Porsche", "model": "911", "rok_produkcji": 2020}},
    "kogoś": {"marka": "Fiat", "model": "Uno", "rok_produkcji": 1997}
}

print(samochody["kizo"])

# zadanie 9

osoby = {
    1: {"imie": "X", "naziwsko": "Y", "samochody": ["audi", "bugatti"]},
    2: {"imie": "A", "naziwsko": "B", "samochody": ["fiat"]},
}

# zadanie 10

panstwa = {
"Polska": {"stolica": "Warszawa", "populacja": 100000, "ustrój": "demokracja"},
"Nowa_Gwinnea": {"stolica": "?", "populacja": "?", "ustrój": "??!"},
}

# zad 11

miasto = {"nazwa": "nazwa","populacja": 1234, "wielkośc": 12345, "atrakcje": []}

panstwa = {
"Polska": {"stolica": {"nazwa": "WWA","populacja": 1234, "wielkośc": 12345, "atrakcje": []}, "populacja": 100000, "ustrój": "demokracja"},
"Nowa_Gwinnea": {"stolica": {"nazwa": "nazwa","populacja": 1234, "wielkośc": 12345, "atrakcje": []}, "populacja": "?", "ustrój": "??!"},
}

print(panstwa.get("Polska").get("stolica").get("nazwa"))
print(panstwa["Polska"]["stolica"]["nazwa"])

# zad 12

uczniowie = {
    "Adam Kowalski": {"waga": 42, "przedmioty": {"weby": 2, "wdp": 6}},
    "Anna Kowalski": {"waga": 32, "przedmioty": {"weby": 2, "wdp": 6}}
}


