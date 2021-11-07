# Rules for finding a closure:
# - we must have a nested function
# - the nested function should reference a value of a higher scope
# - the function that wraps the nested must return it too

# They are used:
# - when we have a class that has only one method
# - when we work with decorators

from typing import Callable


def func_() -> Callable[[], None]:
    a: int = 21

    def nested_func() -> None:
        print(a)
    return nested_func


def multiply_by(x: int) -> Callable[[int], int]:

    def multiplier(n: int) -> int:
        return x*n
    return multiplier


def make_divisor_by(x: int) -> Callable[[int], float]:

    def numerator(n: int) -> float:
        assert n != 0, ZeroDivisionError('Do not divide by zero')
        return n/x
    return numerator


if __name__ == '__main__':
    my_func = func_()
    my_func()  # 21
    del func_
    my_func()  # the nested function remember the a value

    multiply_by_8 = multiply_by(8)
    multiply_by_20 = multiply_by(20)
    print(multiply_by_8(10))  # 80
    print(multiply_by_20(7))  # 140

    divide_by_2 = make_divisor_by(2)
    divide_by_6 = make_divisor_by(6)
    print(divide_by_2(20))  # 10.0
    print(divide_by_6(120))  # 20.0
