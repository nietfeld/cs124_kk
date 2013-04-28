"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""													   ""
""  Coded with love by Emi Nietfeld and Lucas Freitas  ""
""  CS124 - Programming Assignment 3                   ""
""													   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from utils import *
from generate_input import *
import math
max_iter = 25000

def karmarkar_karp(input):
	original = list(input)
	while len(original) > 1:
		distance = abs(original[0] - original[1])
		del original[:2]
		reverse_insort(original, distance)
	print "Karmarkar-Karp: " + str(original[0])

def repeated_random (input): 
	original = list(input)
	iterations = max_iter
	solution = map(lambda x: x * random.randrange(-1, 2, 2), original)
	residual = abs(sum(solution))
	while iterations > 0 and residual > 0:
		new_solution = map(lambda x: x * random.randrange(-1, 2, 2), original)
		new_residual = abs(sum(new_solution))
		if new_residual < residual:
			solution = new_solution
			residual = new_residual
		iterations -= 1
	print "Repeated random: " + str(residual)

def hill_climbing(input):
	original = list(input)
	iterations = max_iter
	length = len(original)
	solution = map(lambda x: x * random.randrange(-1, 2, 2), original)
	residual = sum(solution)
	while iterations > 0 and abs(residual) > 0:
		[i, j] = random.sample(range(length), 2) # pick 2 different indices
		new_residual = residual - 2 * solution[i]
		x = random.randrange(-1, 2, 2)
		new_residual = residual - 2 * solution[j] if x == -1 else residual
		if abs(new_residual) < abs(residual):
			solution[i] *= -1
			solution[j] *= x
			residual = new_residual
		iterations -= 1
	print "Hill climbing: " + str(abs(residual)) 

def T(iter):
	return (10 ** 10) * (0.8 ** math.floor(iter / 300.))

'''def annealing(input):
	original = list(input)
	iterations = max_iter
	length = len(original)
	solution = map(lambda x: x * random.randrange(-1, 2, 2), original)
	best_solution = list(solution)
	residual = sum(solution)
	while iterations > 0 and abs(residual) > 0:
		[i, j] = random.sample(range(length), 2) # pick 2 different indices
		new_residual = residual - 2 * solution[i]
		x = random.randrange(-1, 2, 2)
		new_residual = residual - 2 * solution[j] if x == -1 else residual
		if abs(new_residual) < abs(residual):
			solution[i] *= -1
			solution[j] *= x
			residual = new_residual
			#print new_residual
		else:
			print math.exp(-(abs(new_residual) - abs(residual))/T(max_iter - iterations + 1))

		iterations -= 1
	print "Simulated annealing: " + str(abs(residual)) '''

def main():
	random.seed()
	generate_nums()
	input = readInput("input.txt")
	karmarkar_karp(input)
	repeated_random(input)
	hill_climbing(input)
	#annealing(input)


if __name__ == "__main__":
	main()
