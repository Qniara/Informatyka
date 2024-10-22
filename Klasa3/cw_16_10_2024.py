# Zad.1
# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nzwisko: ")
# with open("dane_osobowe.txt", "w") as plik:
#     plik.write(f"{imie}\n")
#     plik.write(f"{nazwisko}")
# input("Enter wcisnij ")

# Zad.2
# with open("dane_osobowe.txt", "r") as plik:
#     plik2 = list(plik)
# print(f"Witaj {plik2[0].rstrip()} {plik2[1]}")

# Zad.3
# from random import randint
# with open("losowe.txt", "w") as plik:
#     plik2=list(plik)
#     for i in range(10):
#         x=randint(1,100)
#         plik.write(f"{x}")
# print(sum(plik2))
# print(max(plik2))
# print(min(plik2))
# suma=0
# for i in plik2:
#     suma=suma+i

# Zad.4
# plik = open("ciagi.txt", "r")
# plik2 = map(int, list(plik).split("\n"))
# liczba_ciagow = 0
# suma=0
# for ciag in plik2:
#     liczba_ciagow+=1
#     L = map(int, list(ciag).split())
#     for liczba in L:
#         if liczba%2==0:
#             suma+=liczba
# plik.close()
# print(liczba_ciagow)
# print(suma)

# Zad.5
# with open("slowa.txt", "r") as plik:
#     linie = list(plik).rstrip().split()
#     liczba=0
#     for i in range(linie):
#         liczba+=1
#         print(f"{i}. {linie[i]}")
#     print(f"Liczba slow w pliku: {liczba}")
#     for linia in linie:
#         if linia[0]=="a" or linia[0]=="A":
#             print(linia)
