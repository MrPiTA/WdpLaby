a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# 3 3 2

if a > b and a > c or ( a == b > c or a == c > b ):
    if a > b > c:
        print("c < b < a") #
    elif a > c > b:
        print("b < c < a")
    elif a == b > c:
        print("c < b = a ")
    elif a == c > b:
        print("b < c = a")
    elif c == b:
        print("c = b < a")
elif b > a and b > c or ( b == a > c or b == c > a ):
    if b > a > c:
        print("c < a < b")
    elif b > c > a:
        print("a < c < b")
    # elif b == a > c:
    #     print("c < b = a ")
    elif b == c > a:
        print("a < c = b")
    # elif c == b:
    #     print("c = b < a")
if c > a and c > b or ( c == a > b or c == b > a ):
    if c > b > a:
        print("a < b < c")
    elif c > a > b:
        print("b < a < c")
    # elif c == a > b:
    #     print("c < b = a ")
    # elif a == c > b:
    #     print("b < c = a")
    elif a == b:
        print("a = b > c")
elif a == b and a == c:
    print("c = b = a")

