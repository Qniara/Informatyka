# Zad.1
# def DisplayNumbers(L):
#     print(' '.join(map(str, L)))
#
# with open("liczby.txt", "r") as plik:
#     liczby = list(map(int, plik.read().split()))
#     n=len(liczby)+1
#     for i in range(1, n):
#         for j in range(n-i):
#             DisplayNumbers(liczby[j:j+i])
# print(liczby)

# Zad.11
# plik = open("liczby.txt", "r")
# n= plik.readline()
# plik.close()
# dlugoscCiagu = 0
# indexPoczatkowy = 0
# indexmaksa = 0
# maksciag = 0
# for i in range(len(n)-1):
#     if n[i]>=n[i+1]:
#         dlugoscCiagu += 1
#     else:
#         dlugoscCiagu = 0
#     if dlugoscCiagu == 1:
#         indexPoczatkowy = i
#     if dlugoscCiagu > maksciag:
#         maksciag = dlugoscCiagu
#         indexmaksa = indexPoczatkowy
# print(n[indexmaksa:maksciag+indexmaksa:1])

# Sposob sledzia
# plik = open("liczby.txt", "r")
# liczby = list(map(int, plik.read().split()))
# plik.close()
# dlugosc=1
# maksdlugosc = 0
# n= len(liczby)
# for i in range(1,n):
#     if liczby[i]>=liczby[i-1]:
#         dlugosc+=1
#         if dlugosc>maksdlugosc=1
# print(maksdlugosc)

# Zad.12
# plik = open("liczby.txt", "r")
# n= plik.readline()
# plik.close()
# dlugoscCiagu = 0
# indexPoczatkowy = 0
# indexmaksa = 0
# maksciag = 0
# for i in range(len(n)-1):
#     if n[i]<=n[i+1]:
#         dlugoscCiagu += 1
#     else:
#         dlugoscCiagu = 0
#     if dlugoscCiagu == 1:
#         indexPoczatkowy = i
#     if dlugoscCiagu > maksciag:
#         maksciag = dlugoscCiagu
#         indexmaksa = indexPoczatkowy
# print(n[indexmaksa:maksciag+indexmaksa:1])
