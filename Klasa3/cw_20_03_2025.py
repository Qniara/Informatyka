def szybkie_sortowanie(ciag,lewy,prawy):
    i=lewy
    j=prawy
    pivot = ciag[(i+j)//2]
    while i<j:
        while ciag[i]<pivot:
            i+=1
        while ciag[j]>pivot:
            j-=j
        if i<j:
            pom=ciag[i]
            ciag[i]=ciag[j]
            ciag[j]=pom
            i+=1
            j-=1
    if j>lewy:
        szybkie_sortowanie(ciag, lewy, j)
    if i<prawy:
        szybkie_sortowanie(ciag, i ,prawy)

def szybkie_sortowanie2(ciag,lewy,prawy, ciag2):
    i=lewy
    j=prawy
    pivot = ciag[(i+j)//2]
    while i<j:
        while ciag[i]<pivot:
            i+=1
        while ciag[j]>pivot:
            j-=j
        if i<j:
            ciag2[i]=ciag[j]
            ciag2[j]=ciag[i]
            i+=1
            j-=1
    if j>lewy:
        szybkie_sortowanie(ciag, lewy, j)
    if i<prawy:
        szybkie_sortowanie(ciag, i ,prawy)

# Zad.1
# plik = open("liczby.txt", "r")
# liczby = list(map(int, plik.read().split()))
# plik.close()
# lewy=liczby[0]
# prawy=liczby[-1]
# print(szybkie_sortowanie(liczby,lewy,prawy))

# Zad.2
plik = open("liczby", "r")
liczby = list(map(int, plik.read().split()))
plik.close()
ciag=[]
print(szybkie_sortowanie2(liczby,liczby[0],liczby[-1],ciag))
