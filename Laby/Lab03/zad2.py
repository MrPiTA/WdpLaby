
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

n = int(input("Podaj n: "))

# silnia za pomocą pętli for

# silnia = 1
# for i in range(0, n):
#     silnia *= (n-i)
# print(silnia)

# silnia za pomącą while

silnia = 1

while n > 0:
    silnia *= n
    n -= 1
print(silnia)