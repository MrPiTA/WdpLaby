
def find_by_rating(dict, rating):
    for key, value in dict.items():
        if value == rating:
            print(key)


# to do: later refactor all values to 5
songs = {"DISNEY": 5, "KRÓL BALU": 5, "FORMA": 4, "POGO": 2, "MTS": 1}

find_by_rating(songs, 5)


