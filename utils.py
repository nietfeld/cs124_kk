"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""													   ""
""  Coded with love by Emi Nietfeld and Lucas Freitas  ""
""  CS124 - Programming Assignment 3                   ""
""													   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def reverse_insort(a, x, lo = 0, hi = None):
	"""
	Implementation of bisect_left for a list in descending
	order, courtesy of http://tinyurl.com/b8epotx 
	"""
	if lo < 0:
		raise ValueError('lo must be non-negative')
	if hi is None:
		hi = len(a)
	while lo < hi:
		mid = (lo + hi) // 2
		if x > a[mid]: hi = mid
		else: lo = mid + 1
	a.insert(lo, x)

def readInput(filename):
	file = open(filename, "r")
	list = [int(e.strip('\n')) for e in file.readlines()]
	list.sort(reverse=True)
	return list