# Zad.1
T=[0,1,2,3,4,5,6,7,8,9]
a=int(input("Podaj liczbe: "))
# for i in range(10):
#     if a==T[i]:
#         print("tak")
#         a=0
# if a!=0:
#     print

def sortowanie(T):
    temp=0
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i]>T[j]:
                temp=T[j]
                T[j]=T[i]
                T[i]=temp
    return T

def wyszukiwanie_binarne(T,a,n):
    lewy=0
    prawy=n-1
    while lewy<prawy:
        srodek=(lewy+prawy)//2
        if T[srodek]<a:
            lewy=srodek+1
        else:
            prawy=srodek
    return T[lewy]

