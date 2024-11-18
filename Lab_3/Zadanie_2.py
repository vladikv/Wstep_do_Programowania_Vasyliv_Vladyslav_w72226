import string

zdanie = input("Wprowadź zdanie: ")

# a
litery = [char.lower() for char in zdanie if char.isalpha()]
litery_obecne = []

for litera in litery:
    if litera not in litery_obecne:
        litery_obecne.append(litera)

litery_obecne.sort()
litery_brakujace = [litera for litera in string.ascii_lowercase if litera not in litery_obecne]

print("Litery obecne w kolejności alfabetycznej:", ''.join(litery_obecne))
print("Litery, których brak:", ''.join(litery_brakujace))

# b
bez_nieparzystych = ""

for i in range(len(zdanie)):
    if i % 2 == 0:
        bez_nieparzystych += zdanie[i]

print("Zdanie bez znaków o nieparzystych indeksach:", bez_nieparzystych)

# c
slowa = zdanie.split()
wynik = ""

for slowo in slowa:
    if len(slowo) > 1:
        wynik += slowo[0].upper() + slowo[1:-1] + slowo[-1].upper() + " "
    else:
        wynik += slowo.upper() + " "
print("Zdanie z wyrazami zaczynającymi i kończącymi się wielką literą:", wynik.strip())

# d
najdluzsze_slowo = ""

for slowo in slowa:
    if len(slowo) > len(najdluzsze_slowo):
        najdluzsze_slowo = slowo
print(f"Najdłuższe słowo: '{najdluzsze_slowo}', długość: {len(najdluzsze_slowo)}")

# e
zmienione = ""
for i in range(len(zdanie)):
    if zdanie[i] in zdanie[:i]:
        zmienione += "@"
    else:
        zmienione += zdanie[i]
print("Zdanie po zamianie powtórzeń na '@':", zmienione)
