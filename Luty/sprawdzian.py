#Cezar
wyraz = input("Podaj wyraz : ")
zaszyfrowany_wyraz = ""
klucz = int(input("Podaj klucz : "))
for znak in wyraz:
    przesunieta = ord(znak) + klucz #Przesunięta Litera jak co
    poprawka = (przesunieta - ord("a")) % 26 #CHODZI O POPRAWKĘ NA WYPADKU KOŃCU ALFABETU
    zaszyfrowana_litera = chr(poprawka + ord("a"))
    zaszyfrowany_wyraz += zaszyfrowana_litera
print(zaszyfrowany_wyraz)
#NWD - Modulo
a,b = int(input()) , int(input())
while b>0:
    a,b = b, a%b
print(a)
#NWD - Odejmowanie
a, b = int(input()), int(input())
while a != b:
    if a > b : a = a - b
    if b > a : b = b - a
print(a)
#NWW - Modulo
a, b = map(int, input().split())
iloczyn = a * b
while b > 0:
    a, b = b, a%b
nwd = a
print(iloczyn // nwd)
#NWW - odejmowanie
a, b = int(input()), int(input())
iloczyn = a * b
while a != b :
    if a > b : a = a - b
    if b > a : b = b - a
nwd = a
print(iloczyn // nwd)
# Generator liczb pierwszych - liczby pierwsze w przedziale [p, q]

p, q = map(int, input().split())
for i in range(p, q+1):
    flaga = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flaga = False
            break
    if flaga:
        print(i, end=" ")

# Generator liczb pierwszych - początkowe k liczb pierwszych

n = int(input("Podaj ile chcesz liczb pierwszych: "))
x = 2
while n > 0:
    flaga = True
    for i in range(2, x):
        if x % i == 0:
            flaga = False
            break
    if flaga:
        print(x, end=" ")
        n = n - 1
    x = x + 1
#Ułamki

a, b = map(int,input().split("/"))
c, d = map(int,input().split("/"))

x, y = b, d
ilocz = x * y
while y>0:
    x, y = y, x % y
nww = ilocz // x

e = (nww // b) * a
f = (nww // d) * c
g = e + f

print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")