def tower_of_hanoi(n, source, destination, helper):
	if n==1:
		print ("Move disk 1 from peg", source," to peg", destination)
		return
	tower_of_hanoi(n-1, source, helper, destination)
	print ("Move disk",n," from peg", source," to peg", destination)
	tower_of_hanoi(n-1, helper, destination, source)
# n = number of disks
n = 3

tower_of_hanoi(n,' A','C','B')