import math

def poleTrojkata(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return f"Boki muszą być dodatnie"
    elif a+b<=c or a+c<=b or b+c<=a:
        return f"Bład"

    s = (a+b+c)/2
    return round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)

a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

print(f"Pole trojkąta: {poleTrojkata(a,b,c)}")