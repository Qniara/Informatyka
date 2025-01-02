# Zadanie maturalne
def CzyRosnacy(tab):
    n=len(tab)
    for i in range(1,n):
        if(tab[i-1]<tab[i]):
            return False
    return True

def CzyMalejacy(tab):
    n=len(tab)
    for i in range(1,n):
        if not (tab[i-1]<tab[i]):
            return False
    return True

def CzyRosnacoMalejacy(tab):
    n=len(tab)
    if n<4:
        return False
    for k in range(1,n-2):
        if CzyRosnacy(tab[:k+1]) and CzyMalejacy(tab[k+1:]):
            return True
    return False

# Zad.3.3
# plik = open("pi_przyklad.txt","r")
# ciag= list(map(int, plik.read().split()))
# plik.close()
# ile=0
# n=len(ciag)
# for i in range(n-5):
#     if CzyRosnacoMalejacy(ciag[i:i+6]):
#         ile+=1
# print("ile: ", ile)

# Zad.3.4
# plik = open("pi_przyklad.txt","r")
# ciag= list(map(int, plik.read().split()))
# plik.close()
# n=len(ciag)
# maks=4
# poczatek =-1
# for dl in range(4,n):
#     for i in range(n - dl + 1):
#         if CzyRosnacoMalejacy(ciag[i:i + dl]):
#             if dl>maks:
#                 maks=dl
#                 poczatek=i
# print(poczatek+1)
# print(*ciag[poczatek:poczatek+maks], sep="")
