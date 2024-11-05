x = int(input("Podaj pierwsze licbe: "))
y = int(input("Podaj drugie licbe: "))

if x < y:
    while x <= y:
        if x % 2 == 0:
            print(x)
            x += 1
        else:
            x += 1
            continue
else:
    while y <= x:
        if y % 2 == 0:
            y += 1
            print(y)
        else:
            y += 1
            continue