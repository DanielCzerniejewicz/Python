import random
n = int(input())
tab = []
for i in range(n):
    tab.append(random.randint(1,21))
print(tab)

tab.sort()
print(f"Największa liczba : {max(tab)}")

print(f"Najmniejsza liczba : {min(tab)}")

print(f"Ilosc Maksow : {tab.count(max(tab))}")

print(f"Ilość Minimalnych : {tab.count(min(tab))}")

print(f"Rozpiętość : {max(tab) - min(tab)}")

#V-ce max

for i in range(tab.count(max(tab))):
    tab.pop(tab.index(max(tab)))
print(f"V-ce max : {max(tab)}")

#V-ce min

for i in range(tab.count(min(tab))):
    tab.pop(tab.index(min(tab)))
print(f"V-ce min : {min(tab)}")