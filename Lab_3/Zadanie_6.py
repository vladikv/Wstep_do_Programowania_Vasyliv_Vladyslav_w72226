rachunki = {
    "styczeń": 120,
    "luty": 95,
    "marzec": 130,
    "kwiecień": 110,
    "maj": 105,
    "czerwiec": 125,
}

wartosc_maksymalna = max(rachunki.values())
wartosc_minimalna = min(rachunki.values())
suma_wartosci = sum(rachunki.values())
srednia_wartosc = suma_wartosci / len(rachunki)

print("Maksymalna wartość rachunku:", wartosc_maksymalna)
print("Minimalna wartość rachunku:", wartosc_minimalna)
print("Suma wartości rachunków:", suma_wartosci)
print("Średnia wartość rachunku:", round(srednia_wartosc, 2))

# b
ostatni_miesiac = list(rachunki.keys())[-1]
ostatni_rachunek = rachunki[ostatni_miesiac]

if ostatni_rachunek > srednia_wartosc:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")
