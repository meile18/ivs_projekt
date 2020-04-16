# IVS - mathematical library
# Author: Michal Machač, xmacha72
# Date: 21.02.2020

## @package matlib
#  Documentation for this package.

#  Naming conventions for operands available on:
#  https://en.wikipedia.org/wiki/Multiplication


##
# @brief Adds two numbers together.
# @param x Augend.
# @param y Addend.
# @return Sum of x and y.
def add(x, y):
    return x + y


##
# @brief Subtracts y from x.
# @param x Minuend.
# @param y Subtrahend.
# @return Difference of x and y.
def sub(x, y):
    return x - y


##
# @brief Multiplies two numbers.
# @param x Multiplier.
# @param y Multiplicand.
# @return Product of x and y.
def mul(x, y):
    return x * y


##
# @brief Divides x by y.
# @param x Numerator.
# @param y Denominator.
# @return Quotient of x and y.
def div(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x / y


##
# @brief Calculates factorial of given number.
# @param n Number to calculate factorial for.
# @return Factorial of n.
def factorial(n):
    if isinstance(n, int):
        if n > 1:
            return n * factorial(n-1)
        else:
            return 1
    else:
        raise ValueError("n has to be natural number")


##
# @brief Raises x to the power of n.
# @param x Base.
# @param n Exponent.
# @return Power of x to n.
def pow(x, n):
    if isinstance(n, int) and n >= 0:
        return x ** n
    else:
        raise ValueError("n has to be natural number")


##
# @brief Calculates nth root of x.
# @param x Radicand.
# @param n Degree
# @return Nth root of x.
def sqrt(x, n):
    if n <= 0 or x < 0:
        raise ValueError
    else:
        return round(x ** (1/float(n)), 13)


##
# @brief Calculates modulo division.
# @param x Dividend.
# @param n Division.
# @return Remainder of division
def modulo(x, n):
    return x % n



