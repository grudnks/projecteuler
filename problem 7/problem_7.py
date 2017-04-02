#!/usr/bin/env python3

def is_prime(n):
    for i in range(2, int(n**0.5+1)):
        if not n % i:
            return False
    return True

def get_prime(n):
	prime_counter, num = 0, 1
	while prime_counter != n:
		num += 1
		if is_prime(num):
			prime_counter += 1
	return num

print(get_prime(10001))
# Answer: 104743
