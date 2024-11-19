import random

def sredniaLiczba(list):
    s = sum(list)
    s/=len(list)
    return s


lenght = int(input("Podaj ilość elementów w liscie: "))
mylist = []

for i in range(lenght):
    mylist.append(random.randint(0, 100))

print(mylist)

s = sredniaLiczba(mylist)
print(f"Srednia liczba lista: {s}")

