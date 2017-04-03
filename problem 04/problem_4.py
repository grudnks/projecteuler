#!/usr/bin/env python3

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_lp(n, m):
    palindrome = 0
    digits = [0, 0]
    n1 = n
    while n1 > 99:
        n2 = m
        while n2 > 99:
            prod = n1*n2
            if prod > palindrome:
                if is_palindrome(prod):
                    palindrome = prod
                    digits = [n1, n2]
            n2 -= 1
        n1 -= 1
    return palindrome, digits

print(get_lp(999, 999))
# Answer: 906609, [993, 913]