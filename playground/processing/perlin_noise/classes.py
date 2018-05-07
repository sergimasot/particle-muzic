from __future__ import division
import random

class myShape(object):
    cicle = 0
    currentCicleFrameCount = 0.
    currentCicleProgressRatio = 0.
    currentCicleQuadEaseInRatio = 0.
    currentCicleQuadEaseOutRatio = 0.
    currentCicleQuartEaseInRatio = 0.
    currentCicleQuartEaseOutRatio = 0.
    
    frameCountPerCicle = 50
    
    r = color(255,0,0)
    g = color(0,255,0)
    b = color(0,0,255)
    matterColors = [r,g,b]
    c = color(0,255,255)
    m = color(255,0,255)
    y = color(255,255,0)
    antimatterColors = [c,m,y]
    
    noiseScale = .006
    noiseAmount = 80
    N = 100
    
    quarkParamsValues={
        'colors':{'0': matterColors, '1' : antimatterColors},
        'wgt':{'2': 6, '1' : 3, '-1' : 3,'-2' : 3},
        'amp':{'1': 1, '2' : 4, '3' : 1}
    }
        
    def __init__(self, radius, color0, type,gen,q3):
        self.r = radius
        self.colors = myShape.quarkParamsValues['colors'][type]
        self.col = self.colors[color0]
        self._set_color()
        self.ampFactor=myShape.quarkParamsValues['amp'][gen]
        self.weight =myShape.quarkParamsValues['wgt'][q3]
        self._noiseSeed = random.randint(1, 99)
        
    @staticmethod
    def updateCurrentCicleProgress():
        myShape.cicle = frameCount//myShape.frameCountPerCicle
        myShape.currentCicleFrameCount = frameCount%myShape.frameCountPerCicle
        myShape.currentCicleProgressRatio = myShape.currentCicleFrameCount/myShape.frameCountPerCicle
        myShape.currentCicleQuadEaseInRatio = myShape.currentCicleProgressRatio**2
        myShape.currentCicleQuadEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**2 + 1
        myShape.currentCicleQuartEaseInRatio = myShape.currentCicleProgressRatio**4
        myShape.currentCicleQuartEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**4 + 1
    
    @staticmethod
    def p3map(value,start1,end1,start2,end2):
        delta1 = end1 - start1
        delta2 = end2 - start2
        return (delta2*(value - start1)/delta1)+start2
    
    @staticmethod
    def randomChoice(list):
        return random.choice(list)
    
    @staticmethod
    def next(item):
        if item in [0,1]:
            return item +1
        elif item == 2:
            return 0
        else:
            return 0
        
    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        if myShape.currentCicleProgressRatio <= 0.5:
            self.noiseAmount = 40*myShape.currentCicleQuadEaseOutRatio*self.ampFactor
        if myShape.currentCicleProgressRatio > 0.5:
            self.noiseAmount = 40*(1-myShape.currentCicleQuadEaseInRatio)*self.ampFactor
            if myShape.currentCicleProgressRatio > 0.97:
                self._noiseSeed = random.randint(1, 99)
            else:
                pass
    
    def _set_color_ex(self):
        if myShape.currentCicleProgressRatio == 0.0:
            self.col = self.colors[int(myShape.cicle)%3]
        else:
            pass
    
    def _set_color(self):
        if myShape.currentCicleProgressRatio == 0.0 and myShape.cicle>0:
            self.col = self.colors[myShape.next(self.colors.index(self.col))]
        else:
            pass
            
    def display(self):
        noFill()
        self._set_color()
        stroke(self.col)
        strokeWeight(self.weight)
        #print(myShape.currentCicleProgressRatio)
        beginShape()
        noiseSeed(self._noiseSeed)
        self._set_noiseAmount()
        for i in range(0,myShape.N+1):
            x = width/2 + self.r*cos(TWO_PI*i/myShape.N)
            y = height/2 + self.r*sin(TWO_PI*i/myShape.N)
            x += self.p3map(noise(myShape.noiseScale*x,myShape.noiseScale*y,0),0,1,-self.noiseAmount,self.noiseAmount)
            y += self.p3map(noise(myShape.noiseScale*x,myShape.noiseScale*y,1),0,1,-self.noiseAmount,self.noiseAmount)
            vertex(x,y)
        endShape()

class myMeson(myShape):
    def __init__(self, radius, color0, type,gen,q3):
        super(myMeson, self).__init__(radius, color0, type,gen,q3)

class myBaryon(myShape):
    def __init__(self, radius, color0, type,gen,q3):
        super(myBaryon, self).__init__(radius, color0, type,gen,q3)

class myLepton(myShape):
    w = color(255,255,255)
    
    def __init__(self, radius, q3):
        self.r = radius
        self.col = myLepton.w
        self.colors = []
        self.ampFactor=myShape.quarkParamsValues['amp']['1']
        self.weight =myShape.quarkParamsValues['wgt']['1']
        self._noiseSeed = random.randint(1, 99)
    
    def _set_color(self):
        pass
    
    

class myParticle(object):  
    quarkParams = {
    'u' : { 'type' : '0', 'gen' : '1', 'q3' : '2' },
    'd' : { 'type' : '0', 'gen' : '1', 'q3' : '-1'},
    'c' : { 'type' : '0', 'gen' : '2', 'q3' : '2' },
    's' : { 'type' : '0', 'gen' : '2', 'q3' : '-1'},
    't' : { 'type' : '0', 'gen' : '3', 'q3' : '2'},
    'b' : { 'type' : '0', 'gen' : '3', 'q3' : '-1'},
    'ubar' : { 'type' : '1', 'gen' : '1', 'q3' : '-2' },
    'dbar' : { 'type' : '1', 'gen' : '1', 'q3' : '1'},
    'cbar' : { 'type' : '1', 'gen' : '2', 'q3' : '-2' },
    'sbar' : { 'type' : '1', 'gen' : '2', 'q3' : '1'},
    'tbar' : { 'type' : '1', 'gen' : '3', 'q3' : '-2'},
    'bbar' : { 'type' : '1', 'gen' : '3', 'q3' : '1'}
    }

    def __init__(self,composition):
        self.composition = composition # array
        self._componentsObjects=[]
        self._addComponents()
    
    def _addComponents(self):
        if self.composition == []: # lepton also check boson!
            self._componentsObjects.append(myLepton(80,1))
        elif self.composition != []:
            for i, q in enumerate(self.composition):
                type = myParticle.quarkParams[q]['type']
                gen = myParticle.quarkParams[q]['gen']
                q3 = myParticle.quarkParams[q]['q3']
                if len(self.composition)==3:  # baryons
                    self._componentsObjects.append(myBaryon(80,i,type,gen,q3))
                if len(self.composition)==2:  #mesons
                    self._componentsObjects.append(myMeson(80,0,type,gen,q3))
                
    def display(self):
        for i, val in enumerate(self._componentsObjects):
            blendMode(ADD)
            self._componentsObjects[i].display()
