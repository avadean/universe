import numpy as np
import numpy.random as npr

import particle as p



class Universe:
    def __init__(self, size=640):
        self.xyHyperAvions = np.zeros((0,2))
        self.xyNullAvions = np.zeros((0,2))
        self.xyFeatherAvions = np.zeros((0,2))

        self.vxyHyperAvions = np.zeros((0,2))
        self.vxyNullAvions = np.zeros((0,2))
        self.vxyFeatherAvions = np.zeros((0,2))

        self.FxyHyperAvions = np.zeros((0,2))
        self.FxyNullAvions = np.zeros((0,2))
        self.FxyFeatherAvions = np.zeros((0,2))

        self.numHyperAvions = 0
        self.numNullAvions = 0
        self.numFeatherAvions = 0

        self.massHyperAvion = p.massHyperAvion
        self.massNullAvion = p.massNullAvion
        self.massFeatherAvion = p.massFeatherAvion

        self.sizeHyperAvion = p.sizeHyperAvion
        self.sizeNullAvion = p.sizeNullAvion
        self.sizeFeatherAvion = p.sizeFeatherAvion

        self.size = size

    def step(self):
        self.updateCoords()
        self.updateForces()
        self.updateVelocities()
        self.updateForces()
        self.updateVelocities()

    def updateCoords(self):
        for i in range(self.numHyperAvions):
            self.xyHyperAvions[i] += self.vxyHyperAvions[i] + 0.5 * self.FxyHyperAvions[i] / self.massHyperAvion
            self.xyHyperAvions[i] %= self.size

        for i in range(self.numNullAvions):
            self.xyNullAvions[i] += self.vxyNullAvions[i] + 0.5 * self.FxyNullAvions[i] / self.massNullAvion
            self.xyNullAvions[i] %= self.size

        for i in range(self.numFeatherAvions):
            self.xyFeatherAvions[i] += self.vxyFeatherAvions[i] + 0.5 * self.FxyFeatherAvions[i] / self.massFeatherAvion
            self.xyFeatherAvions[i] %= self.size

    def updateForces(self):
        for i in range(self.numHyperAvions):
            #self.FxyHyperAvions[i]  = p.calcHyperFeatherAvionForce(xy=self.xyHyperAvions[i],
            #                                                       xyArray=self.xyFeatherAvions)
            self.FxyHyperAvions[i] = p.calcNullHyperAvionForce(xy=self.xyHyperAvions[i],
                                                                xyArray=self.xyNullAvions)
        for i in range(self.numNullAvions):
            #self.FxyNullAvions[i]  = p.calcNullHyperAvionForce(xy=self.xyNullAvions[i],
            #                                                   xyArray=self.xyHyperAvions)
            self.FxyNullAvions[i] = p.calcFeatherNullAvionForce(xy=self.xyNullAvions[i],
                                                                 xyArray=self.xyFeatherAvions)
        for i in range(self.numFeatherAvions):
            #self.FxyFeatherAvions[i]  = p.calcFeatherNullAvionForce(xy=self.xyFeatherAvions[i],
            #                                                        xyArray=self.xyNullAvions)
            self.FxyFeatherAvions[i] = p.calcHyperFeatherAvionForce(xy=self.xyFeatherAvions[i],
                                                                     xyArray=self.xyHyperAvions)

    def updateVelocities(self):
        for i in range(self.numHyperAvions):
            self.vxyHyperAvions[i] += 0.5 * self.FxyHyperAvions[i] / self.massHyperAvion
        for i in range(self.numNullAvions):
            self.vxyNullAvions[i] += 0.5 * self.FxyNullAvions[i] / self.massNullAvion
        for i in range(self.numFeatherAvions):
            self.vxyFeatherAvions[i] += 0.5 * self.FxyFeatherAvions[i] / self.massFeatherAvion

    def addParticles(self, type_, num, energy=1.0):
        if type_ == 'hyperAvion':
            for _ in range(num):
                x = (2.0 * npr.random(num) - 1.0) * self.size
                y = (2.0 * npr.random(num) - 1.0) * self.size
                self.xyHyperAvions = np.vstack([self.xyHyperAvions, (x, y)])

                vx = (2.0 * npr.random(num) - 1.0) * energy
                vy = (2.0 * npr.random(num) - 1.0) * energy
                self.vxyHyperAvions = np.vstack([self.vxyHyperAvions, (vx, vy)])

                self.FxyHyperAvions = np.vstack([self.FxyHyperAvions, (0.0, 0.0)])

            self.numHyperAvions += num

        elif type_ == 'nullAvion':
            for _ in range(num):
                x = (2.0 * npr.random(num) - 1.0) * self.size
                y = (2.0 * npr.random(num) - 1.0) * self.size
                self.xyNullAvions = np.vstack([self.xyNullAvions, (x, y)])

                vx = (2.0 * npr.random(num) - 1.0) * energy
                vy = (2.0 * npr.random(num) - 1.0) * energy
                self.vxyNullAvions = np.vstack([self.vxyNullAvions, (vx, vy)])

                self.FxyNullAvions = np.vstack([self.FxyNullAvions, (0.0, 0.0)])

            self.numNullAvions += num

        elif type_ == 'featherAvion':
            for _ in range(num):
                x = (2.0 * npr.random(num) - 1.0) * self.size
                y = (2.0 * npr.random(num) - 1.0) * self.size
                self.xyFeatherAvions = np.vstack([self.xyFeatherAvions, (x, y)])

                vx = (2.0 * npr.random(num) - 1.0) * energy
                vy = (2.0 * npr.random(num) - 1.0) * energy
                self.vxyFeatherAvions = np.vstack([self.vxyFeatherAvions, (vx, vy)])

                self.FxyFeatherAvions = np.vstack([self.FxyFeatherAvions, (0.0, 0.0)])

            self.numFeatherAvions += num
