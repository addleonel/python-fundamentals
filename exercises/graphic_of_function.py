import math
import numpy as np
from matplotlib import pyplot as plt


def function(x):
    f = 5*math.pow(x,8)+7*math.pow(x,7)-4*math.pow(x,6)+17*math.pow(x,5)-19*math.pow(x,4)+11*math.pow(x,3)-15*math.pow(x,2)+25*x+11
    return f


def gfunction():
    x = np.array(range(-1000, 1000))
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = function(x[i])

    plt.plot(x, y)
    plt.show()


gfunction()
