# 4 Zad. do dokonczenia
# n = int(input())
# srodek = n//2
# for i in range(n):
#     for j in range(n):
#         #gora
#         if i == 0 and j == srodek:
#             print("*", end="")
#         #dol
#         if i == n-1 and j == srodek:
#             print("*", end="")
#         #lewy cypel
#         if i==srodek and j ==0:
#             print("*", end="")
#         #prawy cypel
#         if i==srodek and j == n-1:
#             print("*", end="")
#         #Lewo
#         if i != srodek and j == srodek:
#         else:
#             print(" ",end="")
#
#     print()
# # 5. Zad
# n = int(input())
# srodek = n//2
# for i in range(n):
#     for j in range(n):
#         if j == srodek:
#             print("*", end="")
#         elif i == srodek:
#             print("-", end="")
#         else:
#             print(" ", end="")
#     print()
# 6. Zad
# n = int(input())
# srodek = n//2
# for i in range(n):
#     for j in range(n):
#         if j==n-1-i:
#             print("?",end="")
#         elif i==j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# # 7. Zad
# n = int(input())
# srodek = n//2
# for i in range(n):
#     for j in range(n):
#         if i==0:
#             print("*",end="")
#         elif i==n-1:
#             print("*",end="")
#         elif j==0:
#             print("*",end="")
#         elif j==n-1:
#             print("*",end="")
#         elif i==srodek and j==srodek:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()