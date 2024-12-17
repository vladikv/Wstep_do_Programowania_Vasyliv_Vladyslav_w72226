from datetime import datetime


def function(lab_date, kolokwium_date):
    dzis = datetime.now()

    lab_date = datetime.strptime(lab_date, "%d-%m-%Y")
    kolokwium_date = datetime.strptime(kolokwium_date, "%d-%m-%Y")

    dni_od_lab = (dzis - lab_date).days
    dni_do_kolokwium = (kolokwium_date - dzis).days

    lab_date_formatted = lab_date.strftime("%d %B %Y")
    kolokwium_date_formatted = kolokwium_date.strftime("%d %B %Y")

    print(f"Ostatnie laboratoria były: {lab_date_formatted} ({dni_od_lab} dni temu).")
    if dni_do_kolokwium >= 0:
        print(f"Do kolokwium pozostało: {dni_do_kolokwium} dni, data: {kolokwium_date_formatted}).")
    else:
        print(f"Kolokwium już się odbyło ({abs(dni_do_kolokwium)} dni temu, data: {kolokwium_date_formatted}).")



ostatnie_laby = input("Podaj datę ostatnich laboratoriów (dd-mm-yyyy): ")
kolokwium = input("Podaj datę kolokwium (dd-mm-yyyy): ")
function(ostatnie_laby, kolokwium)
