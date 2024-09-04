# Zad.1
#def CzyPierwsza(n):
#    return n%2==0
#n=int(input("Podaj liczbe: "))
#if CzyPierwsza(n)==0:
#    print("tak")
#else:
#    print("nie")

# Zad.2
#def dzielnik(n):
#    if n%2==0:
#        return n
#    else:
#        return 0
#n = int(input("Podaj liczbe: "))
#for i in range(1,n):
#    print(dzielnik(i, " "))

# Zad.3
#def dzielnik(n):
#    if n%2==0:
#        return n
#    else:
#        return 0
#n = int(input("Podaj liczbe: "))
#suma=0
#for i in range(1,n):
#    suma= suma+ dzielnik(i)
#print(suma)

# Zad.4
#def dzielnik(n):
#    if n%2==0:
        #return true
        #    else:
#        return false
#suma=0
#n=int(input("Liczba: "))
#for i in range(n):
#    if dzielnik(n)==true:
#        suma+=1
#print(suma)

# Zad.5
#def pierwsza(n):
#    for i in range(2,n):
#        if n%i==0:
#            return false
#    return true
#n = int(input("Dzielniki: "))
#for i in range(2,n+1):
#    if n%i==0:
#        if pierwsza(i)==false:
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
