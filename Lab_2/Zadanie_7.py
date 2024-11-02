# Zadanie a:
a_imię = input("Imię: ")
print("Witaj ", end = a_imię)

# Zadanie b:
wiek = input("\nWiek: ")
print("Twój wiek to: ", end = wiek)

# Zadanie c:
c_imię = input("\nImię: ")
c_nazwisko = input("Nazwisko: ")
inicjaly = c_imię[0].upper() + "." + c_nazwisko[0].upper() + "."
print(inicjaly)

# Zadanie d:
łańcuch = input("Podaj tekst: ")
print(5 * (łańcuch + " "))

# Zadanie e:
łańcuch_1 = input("Podaj pierwszy tekst: ")
łańcuch_2 = input("Podaj drugi tekst: ")

polaczony_lancuch = łańcuch_1 + łańcuch_2

print("Połączony łańcuch to:", polaczony_lancuch)

# Zadanie f:
f_łańcuch_1 = input("Podaj pierwszy tekst: ")
f_łańcuch_2 = input("Podaj drugi tekst: ")
half_first = len(f_łańcuch_1) // 2
half_second = len(f_łańcuch_2) // 2

f_łańcuch_3 = f_łańcuch_1[:half_first] + f_łańcuch_2[half_second:]

print("Trzeci łańcuch:", f_łańcuch_3)