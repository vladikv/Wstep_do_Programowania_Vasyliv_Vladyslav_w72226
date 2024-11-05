from random import randint

lista = ["adkt", "uvjhbdf", "jiwkkfj"]

krotka = tuple(lista)
print(krotka)

ilosc = 0
sk = 0
skt = 0
s = int(input("Podaj minimalny rozmiar slowa: "))
slowa = []

for el in krotka:
    ilosc += len(el)
    for z in el:
        if z=="k":
            sk += 1
    if "kt" in el: skt += 1

    # if el.find("kt") < 0: skt+=1

    if len(el) >= s:
        slowa.append(el)

print(f"\nLiczba znaków w krotce: {ilosc}")
print(f"W krotce znaleziono {sk} wystapien/nia litery 'k'")
print(f"W krotce znaleziono {skt} 'kt' wystapien/nia na ciągu ")
print(f"Slowa: {slowa}")


import random

n = 3
x = 6
lista = []
slowo=""
dlugosc_slowa = 0

for i in range(n):
    b = randint(1,x)
    # lista.append()
