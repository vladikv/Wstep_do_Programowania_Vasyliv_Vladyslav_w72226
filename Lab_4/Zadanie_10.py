def tower_of_hanoi(n):
	return 2**n - 1

n = int(input("Podaj ilość diskow: "))

print(tower_of_hanoi(n))