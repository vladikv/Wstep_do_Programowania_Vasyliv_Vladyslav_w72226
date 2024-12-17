import math
import keyword

def wfunkcje(modul):

    f = dir(modul)
    print(f"Funkcje i atrybuty w module '{modul.__name__}':")
    for funkcja in f:
        print(f" - {funkcja}")
    print("\n")

wfunkcje(math)
wfunkcje(keyword)

print("Dostępne metody dla tuple:")
print(dir(tuple))