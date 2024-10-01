def CzyPierwsza(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

plik=open("liczby.txt", "r")
liczby=list(map(int, plik.read().split()))
plik.close()

# Zad.1
# n=int(input("Podaj liczbe: "))
# czyPierwsza=[True]*(n+1)
# p=2
# while p*p<=n:
#     if czyPierwsza[p]:
#         for i in range(p*p,n+1,p):
#             czyPierwsza[i]=False
#     p=p+1
# for i in range(2,n+1):
#     if czyPierwsza[i]:
#         print(i, end=" ")

# Zad.2
# n=int(input("Podaj liczbe: "))
# suma=0
# ilosc=0
# czyPierwsza = [True]*(n+1)
# p=2
# while p*p<=n:
#     if czyPierwsza[p]:
#         for i in range(p*p, n+1,p):
#                 czyPierwsza[i]=False
#     p=p+1
# for i in range(2,n+1):
#     if czyPierwsza[i]:
#         suma=suma+czyPierwsza[i]
#         ilosc+=1

# Zad.3
# czy_pierwsza[0] ← fałsz
# czy_pierwsza[1] ← fałsz
# dla i=2,3,...,n wykonuj
#   czy_pierwsza[i] ← prawda
# p ← 2
# dopóki p * p ⩽ n wykonuj
#   jeżeli czy_pierwsza[p]=prawda
#       x=p*p
#       dopóki x<n+1 wykonuj:
#           czy_pierwsza[i] ← fałsz
#           x <- x+p
#   p ← p + 1
# dla i=2,3,...,n wykonuj
#   jeżeli czy_pierwsza[i]=prawda to
#       wypisz i

# Zad.4
# n=len(liczby)
# czyPierwsza = [True]*(n+1)
# p=2
# while p*p<=len(liczby):
#     if czyPierwsza[p]:
#         for i in range(p*p,n+1,p):
#             czyPierwsza[i]=False
#     p+=1
# for i in range(2,n+1):
#     if czyPierwsza[i] and czyPierwsza[i]<=1000:
#         print(czyPierwsza[i], end=" ")

# Zad.5
# a=int(input("Podaj liczbe: "))
# b=int(input("Podaj liczbe: "))
