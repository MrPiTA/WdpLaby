
# tabliczka mnożenia

m = int(input("m: "))
n = int(input("n: "))


for m in range(1,m+1):
    for n in range (1,n+1):
        print(m, "*",n, "=", m*n, end=" | ")
    if m == m:
        print(end="\n")

