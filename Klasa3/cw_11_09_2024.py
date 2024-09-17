# Rozklad na czynniki pierwsze
# n = int(input("Podaj liczbe do rokladu: "))
# czynnik = 2
# while n > 1:
#    while n % czynnik == 0:
#        print(czynnik, end=" ")
#        n = n//czynnik
#    czynnik += 1

# Zad.1
# n = int(input("Podaj liczbe: "))
# czynnik = 2
# while n >1:
#     while n % czynnik == 0:
#         print(czynnik)
#         n = n//czynnik
#     czynnik += 1

# Zad.2
# n = int(input("Podaj liczbe: "))
# czynnik = 2
# suma = 0
# while n >1:
#     while n % czynnik == 0:
#         suma += czynnik
#         n = n//czynnik
#     czynnik += 1
# print(suma)

# Zad.3
# n = int(input("Podaj liczbe: "))
# czynnik = 2
# suma = 0
# temp = 1
# while n >1:
#     while n % czynnik == 0:
#         suma += czynnik
#         n = n//czynnik
#     czynnik += 1
# for i in range(2,suma):
#     if suma % i == 0:
#         print("NIE")
#         temp = 0
# if temp == 1:
#     print("TAK")

# Zad. 4
# def czyJestNaLiscie(lista, x):
#     for i in lista:
#         if i == x:
#             return 0
#     return 1
# n = int(input("Podaj liczbe do rokladu: "))
# lista = []
# czynnik = 2
# while n > 1:
#    while n % czynnik == 0:
#        if czyJestNaLiscie(lista, czynnik):
#            lista.append(czynnik)
#        n = n//czynnik
#    czynnik += 1
# for i in lista:
#     print(i, end=" ")

# Zad. 5
# def sumaCyfr(n):
#     suma=0
#     while n>0:
#         suma=suma+n%10
#         n=n//10
#     return suma
# n = int(input("Podaj liczbe: "))
# czynnik = 2
# suma = 0
# while n >1:
#     while n % czynnik == 0:
#         suma += czynnik
#         n = n//czynnik
#     czynnik += 1
# if sumaCyfr(n)==sumaCyfr(suma):
#     print("TAK")
# else:
#     print("NIE")

# Zad. 5 znowu dupa kupa pupa
# def SumaCyfr(n):
#     suma=0
#     while n>0:
#         suma=suma+n%10
#         n=n//10
#     return suma
# 
#
# def SumaCyfrCzynnikow(n):
#     czynnik = 2
#     suma=0
#     sumaCyfrczynnikow = 0
#     while n > 0:
#         while n % czynnik == 0
#             print(czynnik)
#             suma += SumaCyfr(czynnik)
#             n = n // czynnik
#         czynnik += 1
#     return suma
#
#
# def CzyPierwsza(n):
#     for i in range(2,n):
#         if n % i==0:
#             return 0
#     return 1
#
#
# n = int(input("daj liczbe: "))
# if CzyPierwsza(n)==0 and SumaCyfr(n)==SumaCyfrCzynnikow(n):
#     print(tak)
# else:
#     print("nie")
