# #El Huffmano
slowo = input()
Huffman = []
ilosc = 1
for i in range(len(slowo)):
    if slowo[i-1] == slowo[i]:
        ilosc += 1
    else:
        Huffman.append(ilosc)
        Huffman.append(slowo[i])
        ilosc = 1
print(Huffman)
# # El reverso huffmano
slowo = input()
Huffman = []
ilosc = 0
for i in range(len(slowo)):
    if slowo[i].isdigit():
        ilosc = int(slowo[i])
        for j in range(ilosc):
            Huffman.append(slowo[i+1])
print(Huffman)