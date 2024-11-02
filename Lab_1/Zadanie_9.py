wiek = int(input("Ile masz lat?"))

if(wiek < 0) or (wiek > 150):
    print("bląd")
elif(wiek <= 4):
    print("Wstęp jest bezpłatny")
elif(wiek < 18):
    print("Wstęp jest 10zł")
else:
    czy_student = input("Czy jesteś studentem: ").lower()

    if(czy_student == "tak"):
        print("Wstęp jest 15zł")
    else:
        print("Wstęp jest 20zł")