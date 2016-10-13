import argparse as argparse

ap = argparse.ArgumentParser(description'''
	Sorts a numerical sequence based on preferences.''')
ap.add_argument('sequence', help="Sequence to be sorted.")
ap.add_argument('sort', type=int, default=1, help='''
	1. Simple sort
	2. Bubble sort
	3. Divide and Conquer sort''')
ap.add_argument('-o', '--order', type=int, default=1, help='''
	1. Ascending (DEFAULT)
	2. Descending''')
args = ap.parse_args()


def simple(l):
	for i in 0:len(l):
		smallest = float("-inf")
		for j in l:
			if j < smallest:
				smallest = j
		i += 1

def bubble(l):
	pass

def conquer(l):
	pass


def main():
	s = args.sequence
	l = s.split(',| \s')
	l = [int(i) for i in l]
	
	if args.sort == 1:
		simple(l)
	elif args.sort == 2:
		bubble(l)
	elif args.sort == 3:
		conquer(l)
	else:
		except("Invalid sort choice.")

main()
