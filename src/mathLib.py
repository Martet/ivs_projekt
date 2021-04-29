"""!@package mathLib
    @brief Library dedicated to basic arithmetical functions

    Mathematical library containing ADD, SUB, MUL, DIV, POW, SQRT, ROOT, FACT, ABS and RAND functions
    @date April 2021
"""

import math
import random

def ADD(x, y):
    """!
        @brief Adds two numbers

        @param x The first summand
        @param y The second summand
        @return return The sum
    """
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = x + y
        return result
    else:
        raise TypeError("Invalid input")

def SUB(x, y):
    """!
        @brief Subtracts y from x

        @param x The minuend
        @param y The subtrahend
        @return result The difference
    """
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = x - y
        return result
    else:
        raise TypeError("Invalid input")

def MUL(x, y):
    """!
        @brief Multiplies two numbers

        @param x The multiplier
        @param y The multiplicand
        @return result The product
    """
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = x * y
        return result
    else:
        raise TypeError("Invalid input")

def DIV(x, y):
    """!
        @brief Divides x with y

        @param x The divident
        @param y The divisor
        @return result The quotient
    """
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        if (x != 0) and (y != 0):
            result = x / y
            return result
        else:
            raise ZeroDivisionError("Can't divide by zero")
    else:
        raise TypeError("Invalid input")

def POW(x, y):
    """!
        @brief Exponentiates x with y

        @param x Number to exponentiate
        @param y The exponent
        @return result The power
    """
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = (x ** y)
        return result
    else:
        raise TypeError("Invalid input")

def SQRT(x):
    """!
        @brief Makes a square root of x

        @param x The radicand
        @return result
    """
    if (isinstance(x,(int,float))) and (isinstance(x,(int,float))):
        result = math.sqrt(x)
        return result
    else:
        raise TypeError("Invalid input")

def ROOT(x, y):
    """!
        @brief Exponentiates number

        @param x The radicand
        @param y The index
        @return result 
    """
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        if x < 0:
            if y % 2 == 1:
                x = abs(x)
                result = POW(x, 1 / y) * (-1)
                return result
            else:
                raise ValueError("Can't root negative number with positive even exponent")
        else:
            result = POW(x, 1 / y)
            return result
    else:
        raise TypeError("Invalid input")

def FACT(x):
    """!
        @brief Makes factorial of x

        @param x Number to exponentiate
        @return result 
    """
    if (isinstance(x,(int,float))):
        if x >= 0:
            result = 1
            for i in range(1, x + 1):
                result *= i
            return result
        raise ValueError("Can't factorial negative number")
    else:
        raise TypeError("Invalid input")

def ABS(x):
    """!
        @brief Creates absolute value

        @param x Number to be made absolute value of
        @return result Absolute value
    """
    if (isinstance(x,(int,float))):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise TypeError("Invalid input")

def RAND(x, y):
    """!
        @brief RNG

        Generates a random number from the <x, y> range 
        @param x Lowest possible number
        @param y Highest possible number
        @return result The randomized number
    """
    if (isinstance(x,(int))) and (isinstance(y,(int))): #no floating point
        if x < y:
            result = random.randint(x, y)
            return result
        else:
            raise ValueError("First value of a range can't be lower than the second one")
    else:
        raise TypeError("Invalid input")
