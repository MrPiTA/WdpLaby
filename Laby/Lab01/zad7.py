a = int(input("a: "))
b = int(input("b: "))
c = int(input("b: "))

print(max(a,b,c)) # 1 sposób

print("") # przejście do nowej lini

if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > b:
    print(c)
if a == b and a == c:
    print("liczby są równe, i wynoszą", a)



