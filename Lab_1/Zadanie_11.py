import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - 4*a*c

if(d == 0):
    x = -b/(2*a)
    print(x)
if(d > 0):
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print(f"Rozwiązania: x1 = {x1}, x2 = {x2}")
if(d < 0):
    print("Brak rozwiązania")