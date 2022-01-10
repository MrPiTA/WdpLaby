def addPlanet(name, density, base):
    """a)"""
    result = []

    if base:

        for record in base:
            result.append(dict(record))

        for i in range(len(base)):
            if name == base[i]["nazwa"]:
                break
            elif name > base[i]["nazwa"]:
                if i < len(base) - 1:
                    continue
                else:
                    result.append({"nazwa": name, "gęstość": density})
                    break
            else:
                result.insert(i, {"nazwa": name, "gęstość": density})
                break
    else:
        result.append({"nazwa": name, "gęstość": density})

    return result


def readPlanet(name, base):
    """b)"""
    for record in base:
        if record["nazwa"] == name:
            return tuple(record.values())


def updatePlanet(name, denstiny, base):
    """c)"""
    result = []

    for record in base:
        if record["nazwa"] == name:
            record["gęstość"] = denstiny
        result.append(record)

    return result


def deletePlanet(density, base):
    """d)"""
    result = []

    for record in base:
        if record["gęstość"] >= density:
            result.append(record)
    return result


def SearchPlanet(name, base):
    """e)"""
    name_values = []
    for record in base:
        name_values.append(record["nazwa"])
    # wyszukiwanie binarne
    low = 0
    high = len(name_values) - 1
    while low <= high:
        mid = (low + high) // 2
        if name_values[mid] == name:
            return mid
        elif name_values[mid] > name:
            # a b c d e
            high = mid - 1
        else:
            low = mid + 1
    return -1


planety = [
    {"nazwa": "Mars", "gęstość": 5.427},
    {"nazwa": "Ziemia", "gęstość": 5.513}
]

# print(addPlanet("Wenus", 5.204, planety))
# print(addPlanet("Merkury", 5.204, planety))

# print(readPlanet("Ziemia", planety))

planety = addPlanet("Wenus", 5.204, planety)
print(planety)

# print(updatePlanet("Wenus", 4.212, planety))
# print(deletePlanet(5.500, planety))
# print(SearchPlanet("Ziemia", planety))
