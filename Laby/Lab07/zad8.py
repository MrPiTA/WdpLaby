

def czy_istnieje_pierwiastek_drugiego_st(n):

    k_d = 1
    k_g = n

    while k_d <= k_g:
        if k_g - k_d <= 1:
            # print("n nie ma pierwiastka drugiego stopnia")
            return "NIE"
        else:
            j = (k_g + k_d) // 2
            if j**2 == n:
                # print(f" {n} jest potęgą dwójki:", j)
                return "TAK"
            elif j**2 > n:
                k_g = j
            else:
                k_d = j


print(czy_istnieje_pierwiastek_drugiego_st(65))