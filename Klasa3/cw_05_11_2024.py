def scal(tab, lewy, srodek, prawy):
    i=lewy
    j=srodek+1
    k=lewy
    while i<=srodek and j<=prawy:
        if tab[i] < tab[j]:
            pom[k] = tab[i]
            i+=1
        else:
            pom[k] = tab[j]
            j+=1
        k+=1
    while i<=srodek:
        pom[k] = tab[i]
        i+=1
        k+=1
    while j<=prawy:
        pom[k] = tab[j]
        j+=1
        k+=1
    for i in range(lewy, prawy,1):
        tab[i]=pom[i]

def sortuj(tab, lewy,prawy):
    if lewy < prawy:
        srodek = (prawy+lewy)//2
        sortuj(tab, lewy,srodek)
        sortuj(tab,srodek,prawy)
        scal(tab,lewy,srodek,prawy)

# Zad.1
# n=input()
# T = list(map(int, n.split(" ")))
# T2 = sortuj(T,T[0], len(T))
# print(T)

# WERSJA 2
def scal2(t1, t2):
    wynik=[]
    i, j = 0, 0
    n1=len(t1)
    n2=len(t2)
    while i<n1 and j<n2:
        if t1[i]<t2[j]:
            wynik.append(t1[i])
            i+=1
        else:
            wynik.append(t2[j])
            j+=1
    wynik.extend(t1[i:])
    wynik.extend(t2[j:])
    return wynik

def sortowanie_przez_scalanie(t):
    n=len(t)
    if n>1:
        srodek=(n-1)//2
        lewy = sortowanie_przez_scalanie(t[:srodek+1])
        prawy = sortowanie_przez_scalanie((t[srodek+1:]))
        return scal2(lewy,prawy)
    return t

# ciag = input("Podaj ciag: ")
# liczby = list(map(int, ciag.split()))
# print(liczby, "\t\t")
# liczby2=sortowanie_przez_scalanie(liczby)
# print(liczby2)



