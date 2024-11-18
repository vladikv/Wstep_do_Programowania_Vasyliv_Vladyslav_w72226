slowo = input("Wprowadź słowo: ")

slowo = slowo.lower()

if slowo == slowo[::-1]:
    print("Podane słowo jest palindromem.")
else:
    print("Podane słowo nie jest palindromem.")
