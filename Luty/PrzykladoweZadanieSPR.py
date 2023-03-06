a = int(input())
b = int(input())
sprawdzanie = 0
def suma_dzielnikow(liczba):
    suma = 0
    for i in range(1, (liczba // 2) + 1):
        if liczba % i == 0:
            suma += i
    return suma
if suma_dzielnikow(a) == b+1:
    sprawdzanie+=1
if suma_dzielnikow(b) == a+1:
    sprawdzanie +=1
if sprawdzanie == 2:
    print("Tak")
else:
    print("Nie")