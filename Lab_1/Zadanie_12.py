x = float(input("Podaj wartość x: "))

if x > 0:
    a_x = 2 * x
elif x == 0:
    a_x = 0
else:  # x < 0
    a_x = -3 * x
print(f"a(x) = {a_x}")

if x >= 1:
    b_x = x ** 2
else:  # x < 1
    b_x = x
print(f"b(x) = {b_x}")

if x > 2:
    c_x = 2 + x
elif x == 2:
    c_x = 8
else:  # x < 2
    c_x = x - 4
print(f"c(x) = {c_x}")
