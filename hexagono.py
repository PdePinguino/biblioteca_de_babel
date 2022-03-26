#!/usr/bin/env python3
"""
Hexagono is a class that emulates the infinite (and recurring) library
from the tale "La biblioteca de Babel" written by Jorge Luis Borges.

Parameters:
symbols: list of characters to be used when generating a book.
max_char: int that is the amount of characters of each book.
path_books: path to where books will be saved.
If path_books does not exist, it is created.

It has two main functions:
(1) generate_books(N) --> it generates N books of max_char length
and saves them to path_books.
(2) generate_until('a string to be matched') --> it generates books of
max_char length until the given string is found inside the book.
"""

import re
import random
import os
from os.path import join


class Hexagono:
	def __init__(self, symbols, max_char=50, path_books='books'):
		self.symbols = symbols
		self.max_char = max_char
		self.path_books = path_books

	def create(self):
		return ''.join(random.choices(self.symbols, k=self.max_char))

	def compare(self, book):
		# compares book with previously created books
		# if book is equal to or contained in any other book, returns True
		# else returns False
		if isinstance(book, str):
			files = os.listdir(self.path_books)
			for i in range(len(files)):
				with open(join(self.path_books, files[i]), 'r') as file:
					prev_book = file.read()
					if re.search(re.escape(book), prev_book):
						return True
			return False
		else:
			return True

	def save(self, book, name, path):
		# saves generated book to path_books as txt file
		with open(join(path, str(name)+'.txt'), 'w') as file:
			file.write(book)

	def create_folder(self, path):
		try:
			os.makedirs(path)
		except FileExistsError:
			print(f"Warning: saving to folder {path} that already exists.")
			pass

	def generate_books(self, N):
		# generates N unique books
		# and saves them to self.path using the index as title
		self.create_folder(self.path_books)
		for i in range(N):
			print("generating book number ", i)
			book = True
			while self.compare(book):
				book = self.create()
			self.save(book, i, self.path_books)

	def generate_until(self, chain):
		# generates books until chain is generated
		generated = False
		i = 0
		while not generated:
			i += 1
			print(f"trying to generate '{chain}' for {i} times")
			book = self.create()
			if re.search(re.escape(chain), book):
				print(f"'{chain}' generated in '{book}' after {i} times!!!")
				generated=True


if __name__ == '__main__':
	alpha = list('abcdefghijklmnopqrstuvwxyz')  # letras del abecedario
	punt =  list(', .')  # coma, espacio, punto

	symbols = alpha + punt
	max_char = 3200
	path_books = 'books'

	hex = Hexagono(symbols, max_char, path_books)
	hex.generate_books(100)
	hex.generate_until('la biblioteca de babel')
