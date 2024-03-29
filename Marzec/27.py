# ZAGADNIENIA Napisy
# - len, for, "foreach", ord, chr
# - indeksy, zakresy
# - konwersje list <-> napis
# - list - sort reverse
# - split, join
# Algorytmy - anagram, palindom, Boyer-Moore
#
# Wszystkie zadania wykonujemy na 26-znakowym
# alfabecie maturalnym: od A (65) do Z (90)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Przykładowe zadania:

# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
print("Zad.1")
slowo = input()
print(slowo[0])
print(slowo[-1])

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
print("Zad.2")
for i in range(1, len(slowo)-1):
    print(slowo[i])

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
print("Zad.3")
print(slowo[-1])
print(slowo[-2])
print(slowo[-3])
print(slowo[-4])
# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis
print("Zad.4")
suma = 0
for item in slowo:
    suma += ord(item)
print(suma)
# 5. Policz ile we wpisanym napisie jest liter A.
print("Zad.5")
ilosc = 0
for item in slowo:
    if item == chr(65):
        ilosc+=1
print(ilosc)

# 6. Podaj dominującą literkę we wpisanym napisie.
# Niech to będzie tylko jedna literka.

# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"

# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)

# 10. Wypisz literki, których nie ma w napisie

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)