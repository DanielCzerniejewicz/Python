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
# Dodawanie
a,b = map(int, input().split("/"))
c,d = map(int, input().split("/"))
x,y = b,d
iloczyn = x*y
while y>0:
    x,y = y, x%b
nww = iloczyn//x
e = (nww//b) * a
f = (nww//d) * c
g = e + f
print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")
# Odejmowanie
a,b = map(int, input().split("/"))
c,d = map(int, input().split("/"))
x,y = b,d
iloczyn = x*y
while y>0:
    x,y = y, x%b
nww = iloczyn//x
e = (nww//b) * a
f = (nww//d) * c
g = e - f
print(f"{a}/{b} - {c}/{d} = {e}/{nww} - {f}/{nww} = {g}/{nww}")
#Mnożenie
a,b = map(int, input().split("/"))
c,d = map(int, input().split("/"))
gora3 = a*c
dol3 = b*d
print(f"{a}/{b} * {c}/{d} = {gora3}/{dol3}")
#Dzielenie
a,b = map(int, input().split("/"))
c,d = map(int, input().split("/"))
gora3 = a*d
dol3 = b*c
print(f"{a}/{b} : {c}/{d} = {gora3}/{dol3}")