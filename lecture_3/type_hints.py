# PEP 484 -- Type Hints
# Type Definition Syntax


def greeting(name: str = "Nothing") -> str:
    """
    The function receives a string an returns a string
    """
    msg: str = "Hello"
    return msg + " " + name


def sum_three_numbers(a: float, b: float, c: float) -> float:
    """
    This function receives three floats and return the sum
    """
    float_type = float  # type aliases
    avg: float_type = (a + b + c)/3

    return avg


if __name__ == "__main__":
    print(greeting())
    print(sum_three_numbers(23.3, 45.1, 9))
