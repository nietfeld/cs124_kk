"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""													   ""
""  Coded with love by Emi Nietfeld and Lucas Freitas  ""
""  CS124 - Programming Assignment 3                   ""
""													   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from utils import *
import random
max_iter = 25

def karmarkar_karp (list):
	while len(list) > 1:
		distance = abs(list[0] - list[1])
		del list[:2]
		reverse_insort(list, distance)
	print list

def hill_climbing (list):
	# need to check on how this works.... 
	solution = map(lambda x: x * random.randrange(-1, 2, 2), list)
	residual = sum(solution)
	for all in range(max_iter):
		[i, j] = random.sample(range(len(list)),2) # pick 2 different indices
		x = random.randrange(-1, 2, 2)
		solution[i] = solution[i] * -1 			   # flip the sign
		solution[j] = solution[j] * x #flip the sign with p = 1/2
		new_residual = sum(solution)
		if abs(new_residual) < abs(residual): 
			residual = new_residual
		else: 
			solution[i] = solution[i] * -1 
			solution[j] = solution[j] * x
	print "hill_climbing:"
	print residual

def repeated_random (list): 
	solution = map(lambda x: x * random.randrange(-1, 2, 2), list)
	residual = sum(solution)
	print residual
	for x in range(max_iter):
		new_solution = map(lambda x: x * random.randrange(-1, 2, 2), list)
		new_residual = sum(new_solution)
		if abs(new_residual) < abs(residual): 
			solution = new_solution
			residual = new_residual
		print residual
	print "repeated_random"
	print residual


def main ():
	karmarkar_karp(readInput("input.txt"))
	repeated_random(readInput("input.txt"))
	hill_climbing(readInput("input.txt"))

if __name__ == "__main__":
	main()
