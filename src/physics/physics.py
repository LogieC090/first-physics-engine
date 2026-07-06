import numpy as np

particles = []
springs = []
e = 0.9
g = 9.8


def findDistance(pos1, pos2):
    #Both pos1 and pos2 are expected to be 2D vectors stored as an array
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]

    Dsquared = dx ** 2 + dy ** 2
    return np.sqrt(Dsquared)

def getLineOfCentres(pos1, pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    
    I = np.array([dx, dy])
    I = I / np.linalg.norm(I)
    return I

def obliqueCollision(p1, p2):
    u1 = p1.getVel()
    u2 = p2.getVel()
    m1 = p1.getMass()
    m2 = p2.getMass()
    I = getLineOfCentres(p1.getPos(), p2.getPos())
    u1i = np.vecdot(u1, I)
    u2i = np.vecdot(u2, I)
    mT = m1 + m2
    totalInitialMomentum = (u1i * m1) + (u2i * m2)
    speedOfApproach = u1i - u2i

    v1i = (totalInitialMomentum - (m2 * e * speedOfApproach)) / mT
    v2i = (totalInitialMomentum + (m1 * e * speedOfApproach)) / mT

    u1j = u1 - (u1i * I)
    u2j = u2 - (u2i * I)

    v1 = v1i + u1j
    v2 = v2i + u2j

    return v1, v2

def calculateForces():
    for particle1 in particles:
        for particle2 in particles:
            if particle2.ID != particle1.ID:
                r1 = particle1.getRadius()
                r2 = particle2.getRadius()
                if findDistance(particle1.getPos(), particle2.getPos()) <= r1 + r2:
                    v1, v2 = obliqueCollision(particle1, particle2)
                    particle1.changeVel(v1)
                    particle2.changeVel(v2)
        particle1.applyGravity()


#Creating the particle claass
class particle:
    _ID = 0
    def __init__(self, initialPos, radius, mass):
        #Initial pos is expected to be a tuple with 2 elements.
        self._mass = mass
        self._x = initialPos[0]
        self._y = initialPos[1]
        self._pos = [self.x, self.y]
        self._pos = np.array(self._pos)
        self._ID = particle._ID
        particle._ID += 1
        
        self._radius = radius

        self._velX = 0
        self._velY = 0
        self._vel = np.array([self._velX, self._velY])

    def getMas(self):
        return self._mass

    def getRadius(self):
        return self._radius

    def setPos(self):
        self._pos = [self._x, self._y]

    def getPos(self):
        return self._pos
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def getVelX(self):
        return self._velX
    
    def getVelY(self):
        return self._velY
    
    def getVel(self):
        return self._vel
    
    def setVel(self):
        self._vel = np.array([self._velX, self._velY])

    def changeVel(self, vel):
        self._velX = vel[0]
        self._velY = vel[1]
        self.setVel()

    def applyGravity(self):
        self.velY += g
        self.setVel()

    def changePos(self, newPos):
        self._x = newPos[0]
        self._y = newPos[1]
        self.setPos()

    def getSpeed(self):
        mag = np.linalg.norm(self._vel)
        return mag


