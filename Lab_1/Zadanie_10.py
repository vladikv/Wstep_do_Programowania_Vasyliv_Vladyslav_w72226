x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(x,y,z)