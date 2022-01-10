

def is_prime(n):
    if n > 1 and type(n) == int:
        for i in range(2,(n//2)+1):
            if n % i == 0:
                return "NIE"
        return "TAK"
    else:
        return "Podano nieprawidłową liczbe"

print(is_prime(90))