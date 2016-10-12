
n = input("Enter position to obtain Fibonacci sequence number: ")

def calcFibonacci(x):
	if (x == 0):
		return 0
	elif (x == 1):
		return 1
	else:
		return calcFibonacci(x - 2) + calcFibonacci(x - 1)

print(calcFibonacci(n))

