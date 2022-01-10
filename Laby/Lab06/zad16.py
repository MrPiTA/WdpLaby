
def czy_dodatnie(a, b = 1, c = 1, d = 1, e = 1, f = 1):
    """Funkcja ma 1 arg obowiązkowy i resztę nie obowiązkową"""
    iloczyn = a*b*c*d*e*f
    if iloczyn > 0:
        return 1
    else:
        return 0

def czy_trojkat(a,b,c):
    """Aby był trójkąt należy sprawdzić czy najdłuższy odcinek jest krótszy od sumy dwóch pozostałych"""
    if czy_dodatnie(a,b,c) == True:
        if max(a,b,c) < ((a+b+c) - max(a,b,c)):
            return 1
    return 0


print(czy_trojkat(3,3,3))