def CzyPierwsza(n):
    for i in range(2,n):
        if n % i==0:
            return 0
    return 1


plik = open("liczby1.txt","r")
liczby = list(map(int,plik.read().split()))
plik.close()
ile=0
for liczba in liczby:
    if CzyPierwsza(liczba)==1:
        ile+=1
print(ile)