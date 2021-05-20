from numba import njit

import numpy as np
import numpy.random as npr


epsilonHyperFeather = 500.0  #########################
sigmaHyperFeather = 5.0     #########################
sigmaFifteenHyperFeather = 15.0 * sigmaHyperFeather ** 15.0
sigmaSevenHyperFeather = 7.0 * sigmaHyperFeather ** 7.0

epsilonFeatherNull = 500.0  #########################
sigmaFeatherNull = 15.0     #########################
sigmaFifteenFeatherNull = 15.0 * sigmaFeatherNull ** 15.0
sigmaSevenFeatherNull = 7.0 * sigmaFeatherNull ** 7.0

epsilonNullHyper = 500.0  #########################
sigmaNullHyper = 10.0     #########################
sigmaFifteenNullHyper = 15.0 * sigmaNullHyper ** 15.0
sigmaSevenNullHyper = 7.0 * sigmaNullHyper ** 7.0

massHyperAvion = 1.01
massNullAvion = 1.0
massFeatherAvion = 0.97

sizeHyperAvion = 2
sizeNullAvion = 5
sizeFeatherAvion = 3



def calcHyperFeatherAvionForce(xy, xyArray, epsilon=epsilonHyperFeather,
                               fifteenSigma=sigmaFifteenHyperFeather, sevenSigma=sigmaSevenHyperFeather):
    return calcSixteenEightPotential(xy, xyArray, epsilon=epsilon,
                                     fifteenSigmaToTheFifteen=fifteenSigma, sevenSigmaToTheSeven=sevenSigma)

def calcFeatherNullAvionForce(xy, xyArray, epsilon=epsilonFeatherNull,
                               fifteenSigma=sigmaFifteenFeatherNull, sevenSigma=sigmaSevenFeatherNull):
    return calcSixteenEightPotential(xy, xyArray, epsilon=epsilon,
                                     fifteenSigmaToTheFifteen=fifteenSigma, sevenSigmaToTheSeven=sevenSigma)

def calcNullHyperAvionForce(xy, xyArray, epsilon=epsilonNullHyper,
                               fifteenSigma=sigmaFifteenNullHyper, sevenSigma=sigmaSevenNullHyper):
    return calcSixteenEightPotential(xy, xyArray, epsilon=epsilon,
                                     fifteenSigmaToTheFifteen=fifteenSigma, sevenSigmaToTheSeven=sevenSigma)


@njit()
def calcSixteenEightPotential(xy, xyArray, epsilon, fifteenSigmaToTheFifteen, sevenSigmaToTheSeven):

    diffArray = xyArray - xy

    #if diffArray.size == 2:
    #    thetaArray = np.arctan2(diffArray[1], diffArray[0])
    #    diff2Array = diffArray ** 2.0
    #    distEightArray = (diff2Array[0] + diff2Array[1]) ** 4.0
    #else:
    thetaArray = np.arctan2(diffArray[:, 1], diffArray[:, 0])
    diff2Array = diffArray ** 2.0
    distEightArray = (diff2Array[:, 0] + diff2Array[:, 1]) ** 4.0

    distSixteenArray = distEightArray * distEightArray

    magFArray = epsilon * (fifteenSigmaToTheFifteen / distSixteenArray - sevenSigmaToTheSeven / distEightArray)

    return np.sum(magFArray * np.cos(thetaArray)), np.sum(magFArray * np.sin(thetaArray))



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
