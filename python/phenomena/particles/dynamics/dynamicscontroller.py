#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from __future__ import division
import abc
from skhep.math import Vector3D, LorentzVector

class DynamicsController(object):

    def __init__(self, particle, dynamicsclasslist):
        self._particle = particle
        self._setDynamicsList(dynamicsclasslist)

    def _setDynamicsList(self, dynamicsclasslist):
        '''
        Sets list of all dynamics objects
        '''
        objectlist = []
        for transformationclass in classlist:
            objectlist.append(transformationclass(self._particle))
        self._dynamicslist = objectlist

    def updateAcceleration(self,dt):
        '''
        The acceleration is the sum of accelerations of every DynamicType
        '''
        acceleration = Vector3D()
        for dynamic in self._dynamicslist:
            acceleration += dynamic.getAcceleration(dt)
        return acceleration

class DynamicType(object):
    '''
    Abstratc class for itema in the dynamic list
    '''
    def getAcceleration(self,dt):
        return self._acceleration

class MagneticField(DynamicType):

    def __init__(self,particle):
        self._B = Vector3D(0,1,0)
        self._particle = particle
        self._setForce(particle)
        self._setAcceleration()

    def _setForce(self, particle):
        self._Bforce = self._particle.charge * self._particle.fourMomentum.boostVector.cross(self.B)

    def _setAcceleration(self):
        self._acceleration = self._Bforce/self._particle.mass

class ElectricField(DynamicType):

    def __init__(self,particle):
        self._E = Vector3D(0,0,1)
        self._particle = particle
        self._setForce(particle)
        self._setAcceleration()

    def _setForce(self, particle):
        self._Eforce = self._particle.charge * self._E

    def _setAcceleration(self):
        self._acceleration = self._Eforce/self._particle.mass

class Inonization(DynamicType):

    DENSITY =

    def __init__(self, particle):
        self._particle = particle


    def _BetheBlock(self,beta):
        return -2.1*BubbleChamberMedium.DENSITY/beta**2
