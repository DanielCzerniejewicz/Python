import math
def sumacyfr(n):
    suma = 0
    while n != 0:
        suma += n % 10
        n = n // 10
    return suma


for i in range(10, 100):
    gora = sumacyfr(i)
    dol = i
    gcd = math.gcd(gora,dol)
    gora2 = gora//gcd
    if gora2 == 1:
        print(gora2 , dol//gcd)