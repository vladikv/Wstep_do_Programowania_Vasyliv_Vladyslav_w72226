file_name = input("Podaj nazwę pliku: ")

if file_name.endswith((".xls", ".xlsx")):
    print("Plik jest arkuszem Excel.")
else:
    print("Plik nie jest arkuszem Excel.")
