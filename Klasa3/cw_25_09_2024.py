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
# def sito_eratostenesa(n):
#     czyPierwsza = [True] * (n + 1)
#     p = 2
#     while p * p <= n:
#         if czyPierwsza[p]:
#             for i in range(p * p, n + 1, p):
#                 czyPierwsza[i] = False
#         p += 1
#     return czyPierwsza
# 
# def liczbyWprzedziale(a, b):
#     czyPierwsza = sito_eratostenesa(b)
#     liczby_pierwsze = [i for i in range(a, b + 1) if czyPierwsza[i]]
#     return liczby_pierwsze
# 
# a = int(input("Podaj liczbę: "))
# b = int(input("Podaj liczbę: "))
# if a > 2 and a < b:
#     liczby_pierwsze = liczbyWprzedziale(a, b)
#     print("Liczby pierwsze z przedziału [", a, ",", b, "]:")
#     print(liczby_pierwsze)
#     liczba_pierwszych = len(liczby_pierwsze)
#     suma_pierwszych = sum(liczby_pierwsze)
#     print("Liczba liczb pierwszych:", liczba_pierwszych)
#     print("Suma liczb pierwszych:", suma_pierwszych)
# else:
#     print("Podano nieprawidłowy przedział. Upewnij się, że 2 < a < b.")

# Zad.6
# def sito_eratostenesa(n):
#     czyPierwsza = [True] * (n + 1)
#     czyPierwsza[0] = czyPierwsza[1] = False
#     p = 2
#     while p * p <= n:
#         if czyPierwsza[p]:
#             for i in range(p * p, n + 1, p):
#                 czyPierwsza[i] = False
#         p += 1
#     return [i for i in range(2, n + 1) if czyPierwsza[i]]

# liczby_pierwsze = sito_eratostenesa(1000)
# print(f"Liczby pierwsze <= 1000: {liczby_pierwsze}")
# print(f"Liczby z pliku: {liczby}")
# liczby_pierwsze_z_pliku = [liczba for liczba in liczby if liczba in liczby_pierwsze]
# liczba_liczb_pierwszych = len(liczby_pierwsze_z_pliku)
# liczba_wszystkich_liczb = len(liczby)
# if liczba_wszystkich_liczb > 0:
#     procent_liczb_pierwszych = (liczba_liczb_pierwszych / liczba_wszystkich_liczb) * 100
# else:
#     procent_liczb_pierwszych = 0
# print(f"Liczba liczb pierwszych w pliku: {liczba_liczb_pierwszych}")
# print(f"Procent liczb pierwszych: {procent_liczb_pierwszych:.2f}%")
