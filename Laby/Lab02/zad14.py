# NWD

a = int(input("a: "))
b = int(input("b: "))

# while a > b or b > a:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#
# print("NWD tych liczba to: ", a)

# lepszy

while a > b or b > a:
    if a > b:
        a = a % b
        if a == 0:
            a = b
            break
    else:
        b = b % a
        if b == 0:
            break

print("NWD tych liczba to: ", a)