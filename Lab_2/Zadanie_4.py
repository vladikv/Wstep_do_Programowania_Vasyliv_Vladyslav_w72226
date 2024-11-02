n = int(input("n = "))

if n < 0:
    print("Silnia jest zdefiniowana tylko dla liczb naturalnych.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"Silnia liczby {n} to: {factorial}")