zakupy = {"chleb":5.0, "maslo":7.0, "czekolada":12, "czipsy":12.0, "górivka":40.0}

suma = 0
print(zakupy)

for el in zakupy:
    suma+=zakupy[el]
    print(f"{el} za {zakupy[el]} zł")

print(suma)