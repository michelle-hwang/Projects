import sys

n = sys.argv[1]
pi = 3 + (16 / 113) # Gardner's geometric construction of pi
print(("%." + str(n) + "f") % pi)
