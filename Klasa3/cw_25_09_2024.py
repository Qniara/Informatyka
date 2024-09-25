def CzyPierwsza(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

# plik=open("liczby.txt", "r")
# liczby=list(map(int, plik.read().split()))
# plik.close()

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
