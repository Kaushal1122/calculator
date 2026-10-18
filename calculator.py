def validate_inputs(a,b):
    for value in (a,b):
        if isinstance(value,bool) or not isinstance(value,int) or value<=0:
            raise ValueError("Inputs must be positive integers")

def add(a,b):
    validate_inputs(a,b)
    return a+b

def subtract(a,b):
    validate_inputs(a,b)
    return a-b

def multiply(a,b):
    validate_inputs(a,b)
    return a*b
