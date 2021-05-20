from numba import njit

import numpy as np
import numpy.random as npr





'''
@njit
def calcInverseQuartic(x, y, xList, yList, sign=1):
    n = len(xList)

    F = np.array((0.0, 0.0))

    if sign == 1:
        for i in range(n):
            theta = np.arctan2(yList[i] - y, xList[i] - x)
            dist2 = (xList[i] - x) ** 2.0 + (yList[i] - y) ** 2.0
            dist4 = dist2 * dist2
            magnitudeF = 1.0 / dist4
            F += np.array((magnitudeF * np.cos(theta), magnitudeF * np.sin(theta)))

    else:
        for i in range(n):
            theta = np.arctan2(yList[i] - y, xList[i] - x)
            dist2 = (xList[i] - x) ** 2.0 + (yList[i] - y) ** 2.0
            dist4 = dist2 * dist2
            magnitudeF = 1.0 / dist4
            F -= np.array((magnitudeF * np.cos(theta), magnitudeF * np.sin(theta)))

    return F
'''
