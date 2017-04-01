#!/usr/bin/env python3

def get_fib(n):
	a, b = 0, 1
	for i in range(n):
		b, a = a + b, b
	return b

def is_even(n):
	return n % 2 == 0

def get_even_fib_sum(border):
	_sum, n, f = 0, 1, 1
	while f < border:
		f = get_fib(n)
		if is_even(f):
			_sum += f
		n += 1 
	return _sum

print(get_even_fib_sum(4000000))
# Answer: 4613732