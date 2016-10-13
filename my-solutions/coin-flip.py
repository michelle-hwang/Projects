import random

n = input("How many times will you flip the coin?")

choices = [1, 0]
results = list()
for i in (1:n):
	results.append(random.choice(choices))

print("heads: " + sum(choices), "tails: " + n - sum(choices))
		
