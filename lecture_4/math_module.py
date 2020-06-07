# In this session I'm going to use the math module, also I will use its functions

import math

z = math.sqrt(100)
print(z)
# ceil
print(math.ceil(23.2))
print(math.ceil(-23.2))
# x take the sign of y
# math.copysign(x, y)
print(math.copysign(z, -0.0))
# absolute value
print(math.fabs(-12))
# factorial
print(math.factorial(10))
# floor
print(math.floor(23.2))
print(math.floor(-23.2))
# fsum
print(math.fsum([1, 2, 3, 4, 5]))  # output 15
print(math.fsum([0.12, 0.23, 0.1, 0.45])) # output: the items sum from the list
# greatest common divisor
print(math.gcd(12, 9))
print(math.gcd(7, 28))
# infinite
print(math.isfinite(0.0))
#
print("here")
print(math.modf(23.14))
# power and logarithmic functions
print(math.exp(1))
print(math.expm1(1))  # output math.exp(1)-1
# with one argument it's natural logarithm
print(math.log(math.e))
# with two argument it's a logarithmic function with (x, base)
print(math.log(math.e, math.e))  # log(x, base)
print(math.log2(123))  # it's more accurate than log(x, 2)
print(math.log10(234))  # it's more accurate than log(x, 10)
# power of a number
print(math.pow(12, 0.5))
# square of a number
print(math.sqrt(12))
# trigonometric function
print("-"*30)
angle_degree = 90
angle_radian = math.radians(angle_degree)
angle_degree = math.degrees(angle_radian)
print(math.sin(angle_radian))
print(math.cos(angle_radian))
print(math.tan(angle_radian))
print(math.asin(0.5))
print(math.acos(0.5))
print(math.atan(0.5))
# hypotenuse

print(math.hypot(math.cos(angle_radian), math.sin(angle_radian)))
x = math.cos(angle_radian)
y = math.sin(angle_radian)
print(math.hypot(x, y)) # output math.hypot(x, y) = 1
print(math.hypot(12, 12))

