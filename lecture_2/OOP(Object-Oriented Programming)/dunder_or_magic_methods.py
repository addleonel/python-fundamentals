# I'm going to use Dunder or magic methods in Python
import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({}, {}. {})'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector((self.y * other.z - self.z * other.y),
                      (self.z * other.x - self.x * other.z),
                      (self.x * other.y - self.y * other.x))

    def lenght(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # less than
    def __lt__(self, other):
        return self.lenght() < other.lenght()

    # greater than
    def __gt__(self, other):
        return self.lenght() > other.lenght()

    # equal to
    def __eq__(self, other):
        return self.lenght() == other.lenght()

    # not equal
    def __ne__(self, other):
        return self.lenght() != other.lenght()

    # less than or equal to
    def __le__(self, other):
        return self.lenght() <= other.lenght()

    # greater than or equal to
    def __ge__(self, other):
        return self.lenght() >= other.lenght()


# out to the class

v1 = Vector(1, 3, 0)
v2 = Vector(2, 5, 1)
v3 = v1 + v2
v4 = v3 + v2
v5 = v3 - v4
v6 = v5 * v4


print('v1 =', v1)
print('v2 =', v2)
print('v3 =', v3)
print('v4 =', v4)
print('v5 =', v5)
print('v6 =', v6)
print("-"*50)
print('|v1| = ', round(v1.lenght(), 2))
print('|v2| =', round(v2.lenght(), 2))
print("Results: ")
print('|v1| < |v2| : {}'.format(v1 < v2))
print('|v1| > |v2| : {}'.format(v1 > v2))
print('|v1| <= |v2| : {}'.format(v1 <= v2))
print('|v1| >= |v2| : {}'.format(v1 >= v2))
print('|v1| != |v2| : {}'.format(v1 != v2))
print('|v1| == |v2| : {}'.format(v1 == v2))
