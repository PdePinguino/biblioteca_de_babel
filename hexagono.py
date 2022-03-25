#!/usr/bin/env python3

import re
import random
import os
from os.path import join


alfa = list('abcdefghijklmnopqrstuvwxyz')  # letras del abecedario
punt =  list(', .')  # coma, espacio, punto
symbols = alfa + punt
max_char = 3200
path_books = 'books'
try:
	os.makedirs(path_books)
except FileExistsError:
	pass

def create():
	return ''.join(random.choices(symbols, k=max_char))

def compare(text):
	if text != True:
		files = os.listdir(path_books)
		for i in range(len(files)):
			with open(join(path_books, files[i]), 'r') as file:
				prev_page = file.read()
				if page == prev_page:
					return True
	else:
		return True

def save(text, name):
	with open(join(path_books, str(name)+'.txt'), 'w') as file:
		file.write(text)

for i in range(400):
	print(i)
	page = True
	while compare(page):
		page = create()
	save(page, i)
