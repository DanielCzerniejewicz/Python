def sumacyfr(n):
  suma = 0
  while n > 0:
    suma += n % 10
    n = n // 10
  return suma


import math
import os

os.remove("szwajcaria.txt")
file = open("szwajcaria.txt", "x")
for i in range(10, 100):
  gora = sumacyfr(i)
  dol = i
  gcd = math.gcd(gora, dol)
  gora2 = gora // gcd
  dol2 = dol // gcd
  if gora2 == 1:
    file.write(f"{gora}/{dol} = {gora2}/{dol2}" + "\n")
file.close()
