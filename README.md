# La biblioteca de Babel

## Hexagono
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

## Credits
Lee el cuento "La biblioteca de Babel" en
https://ciudadseva.com/texto/la-biblioteca-de-babel/
