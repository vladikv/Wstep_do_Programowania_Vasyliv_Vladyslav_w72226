a = float(input("Pierswsza liczba: "))
b = float(input("Druga liczba: "))

d = input("Działanie: ")

if d == "+":
    print(f"Suma: {a+b}")
elif d == "-":
    print(f"Odejmowanie: {a-b}")
elif d == "/":
    print(f"Dzielenie: {a/b}")
elif d == "*":
    print(f"Mnożenie: {a*b}")
else:
    print("Błędne działanie")
