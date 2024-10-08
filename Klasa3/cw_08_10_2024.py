def Wyszukiwanie_Binarne(T, a, n):
    lewy=0
    prawy=n-1
    while lewy < prawy:
        srodek=(lewy+prawy)//2
        if T[srodek]<a:
            lewy=srodek+1
        else:
            prawy=srodek
    return T[lewy]==a

def Wyszukiwanie_Binarne_rek(T, a, lewy,prawy):
    if lewy < prawy:
        srodek=(lewy+prawy)//2
        if T[srodek]<a:
            return Wyszukiwanie_Binarne_rek(T,a,srodek+1,prawy)
        else:
            return Wyszukiwanie_Binarne_rek(T,a,lewy,srodek)
    return T[lewy]==a

def CzyNiemalejacy(T,n):
    for i in range(n-1):
        if T[i]>T[i+1]:
            return False
    return True

T = list(map(int,input("Podaj ciag: ").split()))
a=int(input("Podaj a: "))
if CzyNiemalejacy(T,len(T)):
    print(Wyszukiwanie_Binarne_rek(T,a,0,len(T)-1))
else:
    print("Ciag musi by uporzadkowany malejaca")
