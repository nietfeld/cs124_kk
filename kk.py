"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""													   ""
""  Coded with love by Emi Nietfeld and Lucas Freitas  ""
""  CS124 - Programming Assignment 3                   ""
""													   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from utils import *

def karmarkar_karp (list):
	while len(list) > 1:
		distance = abs(list[0] - list[1])
		del list[:2]
		reverse_insort(list, distance)
	print list

def main ():
	karmarkar_karp(readInput("input.txt"))

if __name__ == "__main__":
	main()
