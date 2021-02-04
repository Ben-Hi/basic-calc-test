# Calculator methods:
#   Add, Subtract, Multiply, Divide
def calc_add(a, b):
    if type(a) is str:
        raise TypeError
    elif type(b) is str:
        raise TypeError
    else:
        return a + b

def calc_sub(a, b):
    if type(a) is str:
        raise TypeError
    elif type(b) is str:
        raise TypeError
    else:
        return a - b

def calc_mul(a, b):
    if type(a) is str:
        raise TypeError
    elif type(b) is str:
        raise TypeError
    else:
        return a * b

def calc_div(a, b):
    if type(a) is str:
        raise TypeError
    elif type(b) is str:
        raise TypeError
    else:
        return a / b