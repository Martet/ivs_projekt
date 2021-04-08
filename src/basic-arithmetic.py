import math

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
                result = pow(x, 1/y) * (-1)
                return result
            else:
                ValueError("Can't root negative number with postivive exponent")
        else:
            result = pow(x, 1/y)
            return result
    else:
        raise TypeError("Invalid input")