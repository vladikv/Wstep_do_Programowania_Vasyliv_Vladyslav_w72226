def czyDodatnie(a):
    if(a > 0):
        print("Liczba jest dodatnia")
    elif a == 0:
        print("Liczba równa się zero")
    else:
        print("Liczba jest ujemna")

a = int(input("Podaj liczbe: "))
czyDodatnie(a)