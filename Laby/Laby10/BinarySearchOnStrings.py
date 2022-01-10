def find(L, target):
    start = 0
    end = len(L) - 1

    while start <= end:
        mid = (start + end) // 2
        if L[mid] == target:
            return mid
        elif L[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


L = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"]  # Needs to be sorted.

print(find(L, "Peter"))

# a b c d e
