# Zad.1
# A = list(map(int, input("Podaj wspolczynniki od a0 do an: ")))
# x = float(input("Podaj x: "))
# n = len(A)-1
# y = A[0]
# potega = 1
# for i in range(1,n+1):
#     potega=potega*x
#     y=y+A[i]*potega
# print(y)

# Zad.4
# Przyklad 1 - ze zmieniona specyfikacja
# y <- A[n]
# potega <- 1
# dla i <- n-1, n-2, ..., 0 wykonuj
#   potega <- potega * x
#   y <- y + A[i] * potega

# Przyklad 2 - ze zmieniona specyfikacja
# y <- A[0]
# dla i <- 1, 2, ..., n wykonuj:
#   y <- x*y+A[i]

# Zad.5

# A = list(map(int, input("Podaj wspolczynniki od an do a0: ")))
# x = float(input("Podaj x: "))
# n=len(A)-1
# y=A[n]
# potega = n
# for i in range(n-1,-1,-1):
#     potega = potega * x
#     y=y+A[i]*potega
# print(y)

# A = list(map(int, input("Podaj: ")))
# x = float(input("Podaj x: "))
# n=len(A)-1
# y=A[n]
# for i in range(1,n+1):
#     y = x*y+A[i]
# print(y)

