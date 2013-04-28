"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""													   ""
""  Coded with love by Emi Nietfeld and Lucas Freitas  ""
""  CS124 - Programming Assignment 3                   ""
""													   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random

def generate_nums ():
	random.seed()
	file = open("input.txt", "w")
	for i in range(100):
		file.write(str(random.getrandbits(64)) + "\n")