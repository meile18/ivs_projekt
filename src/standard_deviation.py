# IVS - standard deviation
# Author: Tomas Kiss, xkisst00
# Date: 22.02.2020

##
# @file standard_deviation.py
# @brief Functions used for calculation of the standard deviation.
# @author Tomas Kiss (xkisst00)

import sys
import matlib
from random import random
# from random import randint

# import cProfile as profile
# import pstats


##
# @brief Generates random numbers into a file. File is used for testing the computation and read in.
# @param number Number of random values to be generated.
def generate_random_numbers(number):
    path = 'data1000.txt'

    try:
        numbers_file = open(path, 'w')
    except IOError:
        print("Can't open file")
        exit(2)

    max = 1000
    min = -1000
    for a in range(number):
        # numbers_file.write(str(randint(-1000, 1000)))
        numbers_file.write(str(random()*(max - min) + min))
        if a != 999:
            numbers_file.write(str('\n'))

    numbers_file.close()


##
# @brief Computes mean of given collection.
# @param values Collection of numeric values in a list.
# @return Computed mean.
def arithmetic_mean(values):
    sum_of_values = 0
    # sum of all values
    for value in values:
        sum_of_values = matlib.add(sum_of_values, value)
    # number of values in list
    n = len(values)
    return matlib.div(sum_of_values, n)


##
# @brief Reads in numbers from standard input. Solves standard deviation for read numbers.
# @return Computed standard deviation.
def solve_deviation():
    # generating random number into the input file
    # generate_random_numbers(1000)

    values = list()
    data = sys.stdin.readlines()

    # reading in numbers from standard input
    for value in data:
        # splitting the line by whitespaces
        for str_to_float in value.split():
            try:
                # trying to convert strings from the line to float
                values.append(float(str_to_float.rstrip()))
            except ValueError:
                # if the string is not a number the program exits with error
                sys.stderr.write("File was containing not numerical values ('"+str_to_float+"') !\n")
                exit(3)

    mean = arithmetic_mean(values)

    # compute the power of 2 for every number in the list
    pow_values = [matlib.pow(number, 2) for number in values]

    sum_of_values = 0
    # sum of all values
    for value in pow_values:
        sum_of_values = matlib.add(sum_of_values, value)

    # returning the computed standard deviation
    return matlib.sqrt(matlib.div(matlib.sub(sum_of_values, matlib.mul(len(values), matlib.pow(mean, 2))),
                                  matlib.sub(len(values), 1)), 2)


if __name__ == '__main__':
    # commented function calls are used for profiling
    # pr = profile.Profile()
    # pr.disable()
    # pr.enable()

    print(solve_deviation())

    # pr.disable()
    # pr.print_stats()
    # pstats.Stats('profile10.profile')

