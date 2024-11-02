wiek = int(input("Ile masz lat?"))

if (wiek > 0) and (wiek < 150):
    if wiek >= 18:
        print("Jesteś pełnoletni")
    else:
        print("Jesteś nie pełnoletni")
else:
    print("Podane dane są niepoprawne")