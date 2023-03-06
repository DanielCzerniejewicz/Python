print("Podaj co robimy : ")
print("1 - Dodawanie")
print("2 - Odejmowanie")
print("3 - Mnozenie")
print("4 - Dzielenie")
print("5 - Modulo")

wybor = int(input())
x = int(input("Podaj 1. liczbę : "))
y = int(input("Podaj 2. liczbę : "))

def dodawanie(x,y):
    return x+y

def odejmowanie(x,y):
    return x-y

def mnozenie(x,y):
    return x*y

def dzielenie(x,y):
    return x/y

def modulo(x,y):
    return x%y

if wybor == 1 or wybor == 2 or wybor == 3 or wybor == 4 or wybor == 5:
    if wybor == 1:
        print(dodawanie(x,y))
    elif wybor == 2:
        print(odejmowanie(x,y))
    elif wybor == 3:
        print(mnozenie(x,y))
    elif wybor == 4:
        print(dzielenie(x,y))
    elif wybor == 5:
        print(modulo(x,y))
else:
    print("No debil")