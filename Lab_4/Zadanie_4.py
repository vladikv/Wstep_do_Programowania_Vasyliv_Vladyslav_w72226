def BMI(wzrost, waga):
    bmi = waga/(wzrost**2)
    return bmi



wzrost = float(input("Podaj swój wzrost w metrach: "))
waga = float(input("Podaj swoje wagę: "))

if(wzrost > 0 and waga > 0):
    bmi = BMI(wzrost, waga)
    if(bmi < 18.5):
        print(f"Twój bmi równe się {bmi}, to jest niedowaga")
    elif bmi>=18.5 and bmi<=24.9:
        print(f"Twój bmi równe się {bmi}, to jest pożądana masa ciała")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"Twój bmi równe się {bmi}, to jest nadwaga")
    else:
        print(f"Twój bmi równe się {bmi}, to jest otyłość")
else:
    print("Błąd")
