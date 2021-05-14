import particle as p


class Universe:
    def __init__(self, size=640):
        self.avions = []
        self.reds = []
        self.blues = []
        self.greens = []
        self.particles = self.avions + self.reds + self.blues + self.greens
        self.size = size

    def step(self):
        for particle in self.particles:
            particle.pos += particle.vel + 0.5 * particle.F / particle.mass
            particle.pos %= self.size

        for particle in self.particles:
            particle.calcForce(self.avions, self.reds, self.blues, self.greens)

        for particle in self.particles:
            particle.vel += 0.5 * particle.F / particle.mass

        for particle in self.particles:
            particle.calcForce(self.avions, self.reds, self.blues, self.greens)

        for particle in self.particles:
            particle.vel += 0.5 * particle.F / particle.mass

    def addParticles(self, particles, particleType):
        if type(particles) is list:
            if particleType == 'avion':
                self.avions += particles
            elif particleType == 'red':
                self.reds += particles
            elif particleType == 'blue':
                self.blues += particles
            elif particleType == 'green':
                self.greens += particles
            else:
                print('Do not know particle type {}.'.format(particleType))
                exit(1)
        elif type(particles) is p.Particle:
            if particleType == 'avion':
                self.avions.append(particles)
            elif particleType == 'red':
                self.reds.append(particles)
            elif particleType == 'blue':
                self.blues.append(particles)
            elif particleType == 'green':
                self.greens.append(particles)
                print('Do not know particle type {}.'.format(particleType))
                exit(1)
        else:
            print('Do not know python type {}.'.format(type(particles)))
            exit(1)

        self.particles = self.avions + self.reds + self.blues + self.greens