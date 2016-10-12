
n = input("Enter number to find prime factors: ")

def factor(n):
	if n == 1 or n == 0:
		print "No primes."
	else:
		if n % 2 == 0:
			print 2
			while n % 2 == 0:
				n = n / 2
		i = 3
		while n > 1:
			while n % i == 0:
				print i
				n /= i
			i += 2

factor(n)
		


