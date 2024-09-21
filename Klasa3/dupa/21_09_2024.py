def dzielniki(n):
    L=[]
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L

def CzyPierwsza(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def SumaDzielnikow(n):
    L = dzielniki(n)
    suma=0
    for l in L:
        summa=suma+l
    return suma

def SumaCyfr(n):
    suma=0
    while n>0:
        suma+=n%10
        n=n//10
    return suma

def Rozklad(n):
    czynnik=2
    L=[]
    while n>1:
        while n%czynnik==0:
            L.append(czynnik)
            n=n//czynnik
        czynnik+=1
    return L

# n= int(input("Podaj liczbe: "))

# L=dzielniki(n)
# print(L)

# suma=0
# for l in L:
#     summa=suma+l
# if suma==n:
#     print("Liczba jest doskonała")
# else:
#     print("Liczba nie jest doskonała")

# a=int(input("Podaj liczbe: "))
# b=int(input("Podaj liczbe: "))
# if CzyPierwsza(a)==True and CzyPierwsza(b)==True:
#     if a>b and a-b==2:
#         print("TAK")
#     elif b>a and b-a==2:
#         print("TAK")
# else:
#     print("NIE")

# a=int(input("Podaj liczbe: "))
# b=int(input("Podaj liczbe: "))
# if SumaDzielnikow(a)==SumaDzielnikow(b):
#     print("TAK")
# else:
#     print("NIE")

# n=int(input("Podaj liczbe: "))
# suma=0
# L=Rozklad(n)
# for l in L:
#     suma=suma+l
# if SumaCyfr(n)==suma:
#     print("TAK")
# else:
#     print("NIE")
