import math

def ADD (x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        result = x + y
        print(result)
    else:
        print("Invalid input")

def SUB (x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        result = x - y
        print(result)
    else:
        print("Invalid input")

def MUL (x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        result = x * y
        print(result)
    else:
        print("Invalid input")

def DIV (x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        if (x != 0) and (y != 0):
            result = x / y
            print(result)
        else:
            print("Division by 0")
    else:
        print("Invalid input")

def POW (x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        result = (x ** y)
        print(result)
    else:
        print("Invalid input")

def SQRT (n): #square root
    if isinstance(n,(int,float)) and isinstance(n,(int,float)):
        result = math.sqrt(n)
        print(result)
    else:
        print("Invalid input")

def ROOT (x, y): #nth root
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        if (x < 0):
            x = abs(x)
            result = pow(x, 1/y) * (-1)
            print(result)
        else:
            result = pow(x, 1/y)
            print(result)
    else:
        print("Invalid input")