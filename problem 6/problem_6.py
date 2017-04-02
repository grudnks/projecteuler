#!/usr/bin/env python3

def get_sum(n):
	return sum([ x for x in range(1, n+1) ])

def get_sq_sum(n):
	return sum([ x**2 for x in range(1, n+1) ])

def get_sum_sq_dif(n):
	return get_sum(n)**2 - get_sq_sum(n)

print(get_sum_sq_dif(100))
# Answer: 25164150
