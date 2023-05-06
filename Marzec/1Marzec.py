# #Konwersja napis <-> lista (list(), join())
# s = input()
# L = list(s)
# print(L) #Mamy liste z s
# #Łączenie join()
# s = "-".join(L)
# print(s)
#Alogrytm na sprawdzanie czy słowo czytane od tylu znaczy to samo
słowo = input()
tab = list(słowo)
tab2 = tab.copy()
tab2.reverse()
if tab==tab2:
    print("Palindron")
else:
    print("Nie")