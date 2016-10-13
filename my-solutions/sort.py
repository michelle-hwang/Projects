import argparse as argparse

ap = argparse.ArgumentParser(description'''
	Sorts a numerical sequence based on preferences.''')
ap.add_argument('sequence', help="Sequence to be sorted.")
ap.add_argument('sort-type', type=int, default=1, help='''
	1. Simple sort
	2. Bubble sort''')
ap.add_argument('-o', '--order', type=int, default=1, help='''
	1. Ascending (DEFAULT)
	2. Descending''')
args = ap.parse_args()


