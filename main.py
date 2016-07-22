#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *

# Write test for code and find the two bugs

def main():
    number = 86
    print prime_factors(number)
    return

def prime_factors(number):
    result = ''
    while number >= 3:
        for i in give_primes(number):
            if number % i == 0:
                number = number / i
                if result != '':
                    result = result + ' * '
                result = result + str(i)
                break
    return result

def give_primes(till_number):
    result_list = []
    if till_number >= 2:
        for i in range(2, till_number + 1):
            prime = True
            for j in range(3, int(round(sqrt(i))) + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                result_list.append(i)
    return result_list

if __name__ == '__main__':
    main()