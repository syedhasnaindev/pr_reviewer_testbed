def add(a,b) :   
    return a + b

def subtract(a,b) :
    return a - b


def multiply(a,b) :
    return a * b


def divide(a,b) :
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a,b) :    
    return a ** b


def modulus(a,b) :
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b


def floor_divide(a,b) :
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b


def square_root(a) :
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return a ** 0.5


def cube_root(a) :
    if a < 0:
        return -(-a) ** (1/3)
    return a ** (1/3)

