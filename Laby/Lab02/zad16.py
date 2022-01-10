
# sprawdza czy daną liczbę n da się rozłożyć na sumę dwóch kwadratów liczb naturalnych

# czy n = a^2 + b^2

n = int(input("n: "))

flag = 0

for a in range(1, (n//2)+1):
    for b in range(1, (n//2)+1):
        if a**2 + b**2 == n:
            print("Tak, dla ", a, "i", b)
            flag += 1

if flag == 0:
    print("nie znaleziono takich liczb")


#

# n = 4045
#
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i*i + j*j == n:
#       print(i,"^2+",j,"^2=",n)