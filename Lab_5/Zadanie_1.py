import random

# Zadanie A
def numer(osoby):
    return random.randint(1, osoby)


osoby = int(input("Podaj liczbę osób w grupie: "))
numer = numer(osoby)
print(f"Szczęśliwy numerek dla grupy to: {numer}")


# Zadanie B

def rocznik(roczniki):
    return random.choice(roczniki)


roczniki = list(map(int, input("Podaj roczniki urodzenia w grupie(oddzielone przecinkami): ").split(",")))
wylosowany_rocznik = rocznik(roczniki)
print(f"Szczęśliwy rocznik to: {wylosowany_rocznik}")


# Zadanie C

def losowanie_totolotka():
    liczby = list(range(1, 50))
    wylosowane = random.sample(liczby, 6)
    return wylosowane


wynik = losowanie_totolotka()
print(f"Wynik: {wynik}")