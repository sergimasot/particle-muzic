from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class Annihilation(Transformation):

    INPUT = ['e+']
    OUTPUT = ['gamma']
    TARGET = 'e-'

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in Annihilation.INPUT:
            self._buildTransfValues()

    def _outputParticles(self):
        return [(1.0, map(ParticleDataSource.getPDGId, Annihilation.OUTPUT)) ]
        return [(1.0, Annihilation.OUTPUT)]
