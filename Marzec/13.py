ciag = input()
stos = []
for i in range(len(ciag)):
    if ciag[i].isdigit():
        stos.append(int(ciag[i]))
    elif ciag[i] == "+":
        a = stos.pop(-1)
        b = stos.pop(-1)
        stos.append(a+b)
    elif ciag[i] == "-":
        a = stos.pop(-1)
        b = stos.pop(-1)
        stos.append(a-b)
    elif ciag[i] == "*":
        a = stos.pop(-1)
        b = stos.pop(-1)
        stos.append(a*b)
    elif ciag[i] == "/":
        a = stos.pop(-1)
        b = stos.pop(-1)
        stos.append(a//b)
print(stos)