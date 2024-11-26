# Zad.1
def DisplayNumbers(L):
    print(' '.join(map(str, L)))

with open("liczby.txt", "r") as plik:
    liczby = list(map(int, plik.read().split()))
    n=len(liczby)+1
    for i in range(1, n):
        for j in range(n-i):
            DisplayNumbers(liczby[j:j+i])
print(liczby)
