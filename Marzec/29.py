#Skróć ułamek
import math
a,b = map(int,input().split("/"))
gcd = math.gcd(a,b)
gora = (a//gcd)
dol = (b//gcd)
print(f"{gora}/{dol}")
#Załóż że ułamek jest niewłaściwy zamień go na liczbę mieszaną i skróć jeśli to możliwe
c,d = map(int,input().split("/"))
calosc = c//d
licznik = c%d
mianownik = d
print(f"{c}/{d} = {calosc} {licznik}/{mianownik}")