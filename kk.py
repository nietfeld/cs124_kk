"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""													   ""
""  Coded with love by Emi Nietfeld and Lucas Freitas  ""
""  CS124 - Programming Assignment 3                   ""
""													   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from utils import *
from generate_input import *
import math
import heapq
import operator
max_iter = 25000

def karmarkar_karp(input):
	h = []
	for x in input:
		heapq.heappush(h, -x)
	while len(h) > 1:
		a = abs(heapq.heappop(h))
		b = abs(heapq.heappop(h))
		dist = abs(a - b)
		heapq.heappush(h, dist)
	return heapq.heappop(h)

def repeated_random (input):
	# get a random solution and calculate its residual
	solution = [x * random.randrange(-1, 2, 2) for x in input]
	residual = abs(sum(solution))

	# try to find better solutions
	iterations = max_iter
	while iterations > 0 and residual > 0:
		# find new solution
		new_solution = [x * random.randrange(-1, 2, 2) for x in input]
		new_residual = abs(sum(new_solution))
		
		# check if solution is better
		if new_residual < residual:
			residual = new_residual
		iterations -= 1
	return residual

def hill_climbing(input):
	# get a random solution and calculate its residual
	solution = [x * random.randrange(-1, 2, 2) for x in input]
	residual = sum(solution)

	# length of the input and number of iterations
	length = len(input)
	iterations = max_iter

	# try to find better solutions
	while iterations > 0 and abs(residual) > 0:
		# pick two different indices
		[i, j] = random.sample(range(length), 2)
		# flip sign of first index
		new_residual = residual - 2 * solution[i]
		# flip sign of second with 0.5 probability
		sign = random.randrange(-1, 2, 2)
		new_residual = new_residual - 2 * solution[j] if sign == -1 else new_residual
		# if the new residual is better, update solution
		if abs(new_residual) < abs(residual):
			solution[i] *= -1
			solution[j] *= sign
			residual = new_residual
		iterations -= 1
	return abs(residual) 

def T(iter):
	return (10 ** 10) * (0.8 ** math.floor(iter / 300.))

def annealing(input):
	# get a random solution and calculate its residual
	solution = [x * random.randrange(-1, 2, 2) for x in input]
	residual = sum(solution)

	# length of the input, number of iterations and S''
	length = len(input)
	iterations = max_iter
	best_solution = list(solution)

	# try to find better solutions
	while iterations > 0 and abs(residual) > 0:
		# pick two different indices
		[i, j] = random.sample(range(length), 2)
		# flip sign of first index
		new_residual = residual - 2 * solution[i]
		# flip sign of second with 0.5 probability
		sign = random.randrange(-1, 2, 2)
		new_residual = new_residual - 2 * solution[j] if sign == -1 else new_residual
		# if the new residual is better, update solution
		if abs(new_residual) < abs(residual):
			solution[i] *= -1
			solution[j] *= sign
			residual = new_residual
		else:
			# probability of moving
			distance = abs(new_residual) - abs(residual)
			t_iter = T(max_iter - iterations + 1)
			probability = math.exp(-distance/t_iter)
			if random.random() <= probability:
				solution[i] *= -1
				solution[j] *= sign
		if abs(residual) < abs(sum(best_solution)):
			best_solution = list(solution)

		iterations -= 1
	return abs(residual)

def main():
	kk = []
	rr = []
	hc = []
	sa = []
	tests = 50
	print "Testing..."
	for i in range(tests):
		print "Test number " + str(i + 1)
		generate_nums()
		input = readInput("input.txt")
		kk.append(karmarkar_karp(input))
		rr.append(repeated_random(input))
		hc.append(hill_climbing(input))
		sa.append(annealing(input))

	# print results in ranking order
	ranking = {"Karmarkar-Karp": sum(kk)/tests, "Repeated random": sum(rr)/tests, "Hill climbing": sum(hc)/tests, "Simulated annealing": sum(sa)/tests}
	ranking = sorted(ranking.iteritems(), key=operator.itemgetter(1))
	
	print "Results in decreasing performance order"
	for method in ranking:
		print method[0] + ": " + str(method[1])

	print "\nKarmarkar-Karp\n"		
	print kk
	print "\nRepeated random\n"
	print rr
	print "\nHill climbing\n"
	print hc
	print "\nSimulated annealing\n"
	print sa



if __name__ == "__main__":
	main()
