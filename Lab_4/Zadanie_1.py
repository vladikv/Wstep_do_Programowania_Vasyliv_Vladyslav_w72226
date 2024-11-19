import math

def poleKola(r):
    pole = math.pi * r * r
    print(f"Pole kola: {pole:.2f}")

r = int(input("Podaj radius kola: "))

if(r>0):
    poleKola(r)
else:
    print("Błąd")
