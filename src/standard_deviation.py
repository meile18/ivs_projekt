# IVS - standard deviation
# Author: Tomas Kiss, xkisst00
# Date: 22.02.2020

##
# @file standard_deviation.py
# @brief Functions used for calculation of the standard deviation.
# @author Tomas Kiss (xkisst00)

import sys
from random import random
from random import randint
import matlib

# import cProfile as profile

##
# @brief Generates random numbers into a file. File is used for testing the computation and read in.
# @param number Number of random values to be generated.
def generate_random_numbers(number):
    path = 'data.txt'
    numbers_file = open(path, 'w')
    max = 1000
    min = -1000
    for a in range(number):
        # numbers_file.write(str(randint(-1000, 1000)))
        numbers_file.write(str(random()*(max - min) + min))
        if a != 9:
            numbers_file.write(str('\n'))

    numbers_file.close()

##
# @brief Computes mean of given collection.
# @param values Collection of numeric values in a list.
# @return Computed mean.
def arithmetic_mean(values):
    sum_of_values = sum(values)
    # number of values in list
    n = len(values)
    return matlib.div(sum_of_values, n)

##
# @brief Reads in numbers from standard input. Solves standard deviation for read numbers.
# @return Computed standard deviation.
def solve_deviation():
    # generating random number into the input file
    generate_random_numbers(10)

    values = list()
    data = sys.stdin.readlines()

    # reading in numbers from standard input
    for value in data:
        values.append(float(value.rstrip()))
    mean = arithmetic_mean(values)

    # compute the power of 2 for every number in the list
    pow_values = [matlib.pow(number, 2) for number in values]

    # returning the computed standard deviation
    return matlib.sqrt(matlib.div(sum(pow_values) - len(values)*matlib.pow(mean, 2), len(values)-1), 2)


if __name__ == '__main__':
    # commented function calls are used for profiling
    # pr = profile.Profile()
    # pr.disable()
    # pr.enable()

    print(solve_deviation())

    # pr.disable()
    # pr.print_stats()
