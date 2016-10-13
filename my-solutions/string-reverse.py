
s = input("Enter string to be reversed: ")

def reverse1(s):
	return s[::-1]

def reverse2(s):
	if len(s) <= 1:
		return s
	return reverse2(s[1:] + s[0])

print reverse1(s)
print reverse2(s)
