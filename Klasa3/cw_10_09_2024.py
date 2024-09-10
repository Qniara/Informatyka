# Zad.1
#def CzyParzysta(n):
#    return n%2==0
#n=int(input("Podaj liczbe: "))
#if CzyParzysta(n)==0:
#    print("tak")
#else:
#    print("nie")

# Zad.2

#Wersja 1
#n=int(input("Podaj liczbe: "))
#for i in range(1,n):
#    if n%i==0:
#        print(n, end=" ")

# Zad.3
#n= int(input("Podaj liczbe: "))
#suma=0
#for i in range(1,n):
#    if n%i==0:
#        suma=suma+i
#print("Suma dzielnikow podanej liczby to ", i)

# Zad.4
#suma=0
#n=int(input("Liczba: "))
#for i in range(n):
#    if n%i==0:
#        suma+=1
#print(suma)

# Zad.5
#def pierwsza(n):
#    for i in range(2,n):
#        if n%i==0:
#            return false
#    return true
#n = int(input("Podaj liczbe: "))
#for i in range(2,n+1):
#    if n%i==0:
#        if pierwsza(i)==true:
#            print(i, end=" ")

# Zad. 6
#def pierwsza(n):
#    for i in range(2,n):
#        if n%i==0:
#            return false
#    return true
#a=int(input("Liczba: "))
#b=int(input("Liczba: "))
#if pierwsza(a)==true and pierwsza(b)==true:
#    if a>b:
#        if a-b==2:
#            print("tak")
#        else:
#            print("nie")
#    if a < b:
#        if b - a == 2:
#           print("tak")
#        else:
#           print("nie")

# Zad.7
#n=int(input("Podaj liczbe: "))
#suma=0
#for i in range(1,n):
#    if n%i==0:
#        suma=suma+i
#if suma==n:
#    print("Liczba jest doskonala")
#else:
#    print("Liczba nie jest doskonala")

# Zad.8
#def sumaDzielnikow(n):
#    for i in range(1,n):
#        if n%i==0:
#            suma=suma+i
#    return suma
#a= int(input("Podaj liczbe: "))
#b= int(input("Podaj liczbe: "))
#sumaA=sumaDzielnikow(a)
#sumaB=sumaDzielnikow(b)
#if a!=b and sumaA==b and sumaB==a:
#    print("tak")
#else:
#    print("nie")
