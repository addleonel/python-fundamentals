

def is_triangle_number(number):
    import math
    return True if math.ceil((1 + 8*number)**0.5) == (1 + 8*number)**0.5 else False