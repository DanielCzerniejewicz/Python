# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
napis = input()
print(napis[0], napis[-1])
# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
print(napis[1:-1])
# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
print(napis[-1])
print(napis[-2])
print(napis[-3])
print(napis[-4])
# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis
waga = 0
for element in napis:
    waga = waga + ord(element)
print(waga)
# 5. Policz ile we wpisanym napisie jest liter A.
ilosc = 0
for element in napis:
    if ord(element) == 65:
        ilosc += 1
print(ilosc)
# 6. Podaj dominującą literkę we wpisanym napisie.
# Niech to będzie tylko jedna literka.
def dominujaca(s):
    return max(set(s), key = s.count)
print(dominujaca(napis))
# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)
# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
suma = 0
for i in range(len(napis)):
    if napis[i] == "L" and napis[i+1] == "A":
        suma+=1
if suma == 3:
    print("TRZY PODCIĄGI LA")
else:
    print(f"Ilość podciągów LA : {suma}")
# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)
suma2 = 0
for item in napis:
    suma2 += ord(item)
srednia = suma2//len(napis)
print(srednia)
# 10. Wypisz literki, których nie ma w napisie
for i in range(65,90):
    if chr(i) in napis:
        pass
    else:
        print(chr(i))
# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)
def palindromy(string):
    return [string[i:i+3] for i in range(len(string) - 2)
            if string[i] == string[i+2] and (string[i:i+3] == string[i:i+3][::-1])]
print(palindromy(napis))