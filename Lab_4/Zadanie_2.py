def poleTrapezu(a,b,h):
    pole = ((a+b)/2) * h
    return pole


a = float(input("Podaj pierwsze strone trapezu: "))
b = float(input("Podaj druge strone trapezu: "))
h = float(input("Podaj wysokość trapezu: "))


if(a > 0 and b > 0 and h > 0):
    pole = poleTrapezu(a, b, h)
    print(f"Pole trapezu: {pole}")
else:
    print("Błąd")