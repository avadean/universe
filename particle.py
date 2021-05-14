from numba import njit

import numpy as np
import numpy.random as npr


@njit
def calcInverseQuartic(x, y, xList, yList):
    n = len(xList)

    F = np.array((0.0, 0.0))

    for i in range(n):
        theta = np.arctan2(yList[i] - y, xList[i] - x)
        dist2 = (xList[i] - x) ** 2.0 + (yList[i] - y) ** 2.0
        dist4 = dist2 * dist2
        magnitudeF = 1.0 / dist4
        F += np.array((magnitudeF * np.cos(theta), magnitudeF * np.sin(theta)))

    return F


def avionGenerator(universeSize, num=0, energy=0.0):
    x0List = (2.0 * npr.random(num) - 1.0) * universeSize
    y0List = (2.0 * npr.random(num) - 1.0) * universeSize
    vx0List = (2.0 * npr.random(num) - 1.0) * energy
    vy0List = (2.0 * npr.random(num) - 1.0) * energy

    return [Avion( x0=x0List[i] ,  y0=y0List[i],
                  vx0=vx0List[i], vy0=vy0List[i])
            for i in range(num)]

def redGenerator(universeSize, num=0, energy=0.0):
    x0List = (2.0 * npr.random(num) - 1.0) * universeSize
    y0List = (2.0 * npr.random(num) - 1.0) * universeSize
    vx0List = (2.0 * npr.random(num) - 1.0) * energy
    vy0List = (2.0 * npr.random(num) - 1.0) * energy

    return [Red( x0=x0List[i] ,  y0=y0List[i],
                vx0=vx0List[i], vy0=vy0List[i])
            for i in range(num)]

def blueGenerator(universeSize, num=0, energy=0.0):
    x0List = (2.0 * npr.random(num) - 1.0) * universeSize
    y0List = (2.0 * npr.random(num) - 1.0) * universeSize
    vx0List = (2.0 * npr.random(num) - 1.0) * energy
    vy0List = (2.0 * npr.random(num) - 1.0) * energy

    return [Blue( x0=x0List[i] ,  y0=y0List[i],
                 vx0=vx0List[i], vy0=vy0List[i])
            for i in range(num)]

def greenGenerator(universeSize, num=0, energy=0.0):
    x0List = (2.0 * npr.random(num) - 1.0) * universeSize
    y0List = (2.0 * npr.random(num) - 1.0) * universeSize
    vx0List = (2.0 * npr.random(num) - 1.0) * energy
    vy0List = (2.0 * npr.random(num) - 1.0) * energy

    return [Green( x0=x0List[i] ,  y0=y0List[i],
                  vx0=vx0List[i], vy0=vy0List[i])
            for i in range(num)]





class Particle:
    def __init__(self, size, color, x0, y0, vx0, vy0, mass):
        self.size = size
        self.color = color

        self.pos = np.array((x0, y0))
        self.vel = np.array((vx0, vy0))
        self.F   = np.array((0.0, 0.0))

        self.mass = mass



class Avion(Particle):
    def __init__(self, x0=0.0, y0=0.0, vx0=0.0, vy0=0.0):
        super().__init__(size=1,
                         color='baby pink',
                         x0=x0,
                         y0=y0,
                         vx0=vx0,
                         vy0=vy0,
                         mass=1.0)

    def calcForce(self, avions, reds, blues, greens):
        pass

class Red(Particle):
    def __init__(self, x0=0.0, y0=0.0, vx0=0.0, vy0=0.0):
        super().__init__(size=5,
                         color='red',
                         x0=x0,
                         y0=y0,
                         vx0=vx0,
                         vy0=vy0,
                         mass=1.0)

    def calcForce(self, avions, reds, blues, greens):
        self.F = 10000.0 * calcInverseQuartic(x=self.pos[0], y=self.pos[1],
                                    xList=np.array([blue.pos[0] for blue in blues]),
                                    yList=np.array([blue.pos[1] for blue in blues]))

        self.F -= -100.0 * calcInverseQuartic(x=self.pos[0], y=self.pos[1],
                                     xList=np.array([green.pos[0] for green in greens]),
                                     yList=np.array([green.pos[1] for green in greens]))

class Blue(Particle):
    def __init__(self, x0=0.0, y0=0.0, vx0=0.0, vy0=0.0):
        super().__init__(size=5,
                         color='blue',
                         x0=x0,
                         y0=y0,
                         vx0=vx0,
                         vy0=vy0,
                         mass=1.0)

    def calcForce(self, avions, reds, blues, greens):
        self.F = 10000.0 * calcInverseQuartic(x=self.pos[0], y=self.pos[1],
                                    xList=np.array([green.pos[0] for green in greens]),
                                    yList=np.array([green.pos[1] for green in greens]))

        self.F -= -100.0 * calcInverseQuartic(x=self.pos[0], y=self.pos[1],
                                     xList=np.array([red.pos[0] for red in reds]),
                                     yList=np.array([red.pos[1] for red in reds]))

class Green(Particle):
    def __init__(self, x0=0.0, y0=0.0, vx0=0.0, vy0=0.0):
        super().__init__(size=5,
                         color='green',
                         x0=x0,
                         y0=y0,
                         vx0=vx0,
                         vy0=vy0,
                         mass=1.0)

    def calcForce(self, avions, reds, blues, greens):
        self.F = 10000.0 * calcInverseQuartic(x=self.pos[0], y=self.pos[1],
                                    xList=np.array([red.pos[0] for red in reds]),
                                    yList=np.array([red.pos[1] for red in reds]))

        self.F -= -100.0 * calcInverseQuartic(x=self.pos[0], y=self.pos[1],
                                     xList=np.array([blue.pos[0] for blue in blues]),
                                     yList=np.array([blue.pos[1] for blue in blues]))
