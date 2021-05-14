import pygame as pg
import time

import particle as p
import universe as u


class Visualiser:
    pg.init()
    pg.display.set_caption("¡Ava's universe! :-}")

    maxFPS = 30
    clock = pg.time.Clock()

    colors = {'black': pg.Color('black'),
              'white': pg.Color('white'),
              'red'  : pg.Color('red'),
              'blue' : pg.Color('blue'),
              'green': pg.Color('green'),

              'baby pink': pg.Color(255, 204, 229),
              'baby blue': pg.Color(153, 255, 255)
              }

    colors['fill'] = colors['baby blue']
    colors['particle'] = colors['black']

    def __init__(self, univeriseSize):
        self.windowWidth = univeriseSize
        self.windowHeight = univeriseSize

        self.screen = pg.display.set_mode((self.windowWidth, self.windowHeight))

        self.running = True

    def drawUniverse(self, universe):
        self.screen.fill(self.colors['fill'])

        for particle in universe.particles:
            pg.draw.circle(self.screen,
                           self.colors[particle.color],
                           particle.pos.astype(int),
                           particle.size)

        pg.display.flip()

    def tickClock(self):
        self.clock.tick(self.maxFPS)

    def quit(self):
        self.running = False





universe = u.Universe()
avions = p.avionGenerator(universe.size, num=1000, energy=10.0)
reds = p.redGenerator(universe.size, num=10, energy=5.0)
blues = p.blueGenerator(universe.size, num=10, energy=5.0)
greens = p.greenGenerator(universe.size, num=10, energy=5.0)

universe.addParticles(avions, 'avion')
universe.addParticles(reds, 'red')
universe.addParticles(blues, 'blue')
universe.addParticles(greens, 'green')












if __name__ == '__main__':
    visual = Visualiser(universe.size)

    while visual.running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                visual.quit()

        universe.step()
        visual.drawUniverse(universe)
        visual.tickClock()
