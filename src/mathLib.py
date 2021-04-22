import math
import random

def ADD(x, y):
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = x + y
        return result
    else:
        raise TypeError("Invalid input")

def SUB(x, y):
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = x - y
        return result
    else:
        raise TypeError("Invalid input")

def MUL(x, y):
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = x * y
        return result
    else:
        raise TypeError("Invalid input")

def DIV(x, y):
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        if (x != 0) and (y != 0):
            result = x / y
            return result
        else:
            raise ZeroDivisionError("Can't divide by zero")
    else:
        raise TypeError("Invalid input")

def POW(x, y):
    if (isinstance(x,(int,float))) and (isinstance(y,(int,float))):
        result = (x ** y)
        return result
    else:
        raise TypeError("Invalid input")

def SQRT(n): #square root
    if (isinstance(n,(int,float))) and (isinstance(n,(int,float))):
        result = math.sqrt(n)
        return result
    else:
        raise TypeError("Invalid input")

def ROOT(x, y): #nth root
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
    if (isinstance(x,(int,float))):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise TypeError("Invalid input")

def RAND(x, y):
    if (isinstance(x,(int))) and (isinstance(y,(int))): #no floating point
        if x < y:
            result = random.randint(x, y)
            return result
        else:
            raise ValueError("First value of a range can't be lower than the second one")

    else:
        raise TypeError("Invalid input")
