
while True:
	try:
		n = input("Enter number of decimal places for pi: ")
		if (n <= 20):
			break
		elif (n >= 0):
			break
	except ValueError:
		print("Number must be between 0 and  21.")

pi = 3 + (16 / 113) # Gardner's geometric construction of pi
print(("%." + str(n) + "f") % pi)
