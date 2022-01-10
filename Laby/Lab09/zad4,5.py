
def replace(d, v, e):
    """zad 4"""
    d[v] = e

def invert(d):
    """zad 5"""
    dlnv = {}
    for key, value in d.items():
        if value not in dlnv:
            dlnv[value] = [key]
        else:
            dlnv[value].append(key)
    return dlnv




d = {1: "a", 2: "c", 3: "c", 4: "d"}

# replace(d, 2, 190)


print(d)
print(invert(d))