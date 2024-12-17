import keyword


def sprawdzennie(lista_slow):
    for slowo in lista_slow:
        if keyword.iskeyword(slowo):
            print(f"'{slowo}' - to jest keyword.")
        else:
            print(f"'{slowo}' - to nie jest keyword.")


slowa = ["for", "print", "break", "done", "bad"]

sprawdzennie(slowa)