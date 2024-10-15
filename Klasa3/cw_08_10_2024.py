def Wyszukiwanie_Binarne(T, a, n):
    lewy = 0
    prawy = n - 1
    while lewy < prawy:
        srodek = (lewy + prawy) // 2
        if T[srodek] < a:
            lewy = srodek + 1
        else:
            prawy = srodek
    return T[lewy] == a


def Wyszukiwanie_Binarne_rek(T, a, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy + prawy) // 2
        if T[srodek] < a:
            return Wyszukiwanie_Binarne_rek(T, a, srodek + 1, prawy)
        else:
            return Wyszukiwanie_Binarne_rek(T, a, lewy, srodek)
    return T[lewy] == a


def CzyNiemalejacy(T, n):
    for i in range(n - 1):
        if T[i] > T[i + 1]:
            return False
    return True

# T = list(map(int,input("Podaj ciag: ").split()))
# a=int(input("Podaj a: "))
# if CzyNiemalejacy(T,len(T)):
#     print(Wyszukiwanie_Binarne_rek(T,a,0,len(T)-1))
# else:
#     print("Ciag musi by uporzadkowany malejaca")

# Zad.3
# plik=open("ciagi.txt")
# ciagi=list(plik.read().split("\n"))
# plik.close()
# for i in ciagi:
#     for j in range(len(i)):
#         if(i[j]=="10"):
#             print(i)
#             break

# Zad.4
# def przetwarzaj_pliki(nazwa_pliku):
#     with open(nazwa_pliku, 'r') as plik:
#         liczba_ciagow = int(plik.readline().strip())

#         for _ in range(liczba_ciagow):
#             liczba_elementow = int(plik.readline().strip())
#             ciag = list(map(int, plik.readline().strip().split()))
#             ciag.sort()
#             if Wyszukiwanie_Binarne(ciag, 10):
#                 print("Ciąg zawierający liczbę 10:", ciag)
# przetwarzaj_pliki('ciagi2.txt')

# Wersja Śledź
# plik=open("ciagi2.txt", "r")
# n=int(plik.readline().rstrip())
# for i in range(n):
#     d=int(plik.readline().rstrip())
#     ciag = list(map(int, plik.readline().split()))
#     if Wyszukiwanie_Binarne(ciag, 10, d):
#         print(ciag)
# plik.close()

# Zad.5
# Funkcja wyszukiwanie_binarne(T, a, n):
#     lewy ← 1
#     prawy ← n
#     dopóki lewy ≤ prawy wykonuj:
#         srodek ← (lewy + prawy) div 2
#         jeżeli T[srodek] = a to:
#             zwróć Prawda
#         w przeciwnym razie jeżeli T[srodek] < a to:
#             lewy ← srodek + 1
#         w przeciwnym razie:
#             prawy ← srodek - 1

#     zwróć Fałsz

# Zad.6
# from random import randint
# T=[]
# pupa=False
# ilosc=0
# T[0]=randint(1,10)
# for i in range(1,1000000):
#     x=randint(1,3)
#     T[i]=T[i-1]+x
#     if T[i]==1500000:
#         pupa=True
#     elif pupa==False:
#         ilosc+=1
# if pupa==True:
#     print("tak ", ilosc)
# else:
#     print("nie")

# Zad.7
A=[0,5,99,3,7,111,13,4,24,4,8]
n=10
i=1
w=0
# OD TĄD JEST ZADANIE
# while i<=n:
#     if A[i]%2==0:
#        w=A[i]
#        break
#     i=i+1
# print(w)
# WERSJA LEPSZA
# lewy = 1
# prawy = n
# while lewy < prawy:
#     srodek = (lewy + prawy) // 2
#     if T[srodek] % 2==1:
#         lewy = srodek + 1
#     else:
#         prawy = srodek
# w=A[lewy]

# PSEUDOKOD
# i <- 1
# dopóki i<=n wykonuj:
#   jeżeli A[i] mod 2 = 0 to:
#       w <- A[i]
#       zwróć w i zakończ
#   i <- i + 1
