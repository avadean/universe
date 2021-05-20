import pygame as pg

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

    colors['hyperAvion'] = colors['red']
    colors['nullAvion'] = colors['blue']
    colors['featherAvion'] = colors['green']

    def __init__(self, univeriseSize):
        self.windowWidth = univeriseSize
        self.windowHeight = univeriseSize

        self.screen = pg.display.set_mode((self.windowWidth, self.windowHeight))

        self.running = True

    def drawUniverse(self, universe):
        self.screen.fill(self.colors['fill'])

        for xyHyperAvion in universe.xyHyperAvions:
            pg.draw.circle(self.screen,
                           self.colors['hyperAvion'],
                           xyHyperAvion,
                           universe.sizeHyperAvion)

        for xyNullAvion in universe.xyNullAvions:
            pg.draw.circle(self.screen,
                           self.colors['nullAvion'],
                           xyNullAvion,
                           universe.sizeNullAvion)

        for xyFeatherAvion in universe.xyFeatherAvions:
            pg.draw.circle(self.screen,
                           self.colors['featherAvion'],
                           xyFeatherAvion,
                           universe.sizeFeatherAvion)

        pg.display.flip()

    def tickClock(self):
        self.clock.tick(self.maxFPS)

    def quit(self):
        self.running = False





universe = u.Universe()

universe.addParticles(type_='hyperAvion', num=2, energy=3.0)
universe.addParticles(type_='nullAvion', num=2, energy=3.0)
universe.addParticles(type_='featherAvion', num=2, energy=3.0)












if __name__ == '__main__':
    visual = Visualiser(universe.size)

    while visual.running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                visual.quit()

        universe.step()
        #print(universe.xyNullAvions, 'null')
        #print(universe.xyFeatherAvions, 'feather')
        #print(universe.xyHyperAvions, 'hyper')
        visual.drawUniverse(universe)
        visual.tickClock()
