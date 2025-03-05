# Zad.2
# wsp = list(map(int, input("Podaj ciag liczb: ").split()))
# x = int(input("Podaj x: "))
# print(wsp, x)
# n = len(wsp)
# stopien = n -1
# w = wsp[n-1]
# for i in range(n-2, -1, -1):
#     w = w*x+wsp[i]
# print(w)

# Zad.4
plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().split()))
plik.close()
print(liczby)
dlugosc=0
maxdlugosc=0
for i in range(len(liczby)):
    
