def potega(a,n):
    if n==0:
        return 1
    elif n<0:
        return 1/potega(a,-n)
    elif n<0 and a<0:
        return -(1/potega(a,-n))
    return a * potega(a, n-1)

a = int(input("Podaj liczbe a: "))
n = int(input("podaj potęge: "))

print(potega(a,n))