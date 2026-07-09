import numpy as np

particles = []
springs = []
e = 0.9
eFloor = 0.3
g = 980
collisionLeaniance = 1

with open("src/data.txt", "r") as file:
    data = file.readlines()

WIDTH = int(data[0])
HEIGHT = int(data[1])
fps = int(data[2])

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
    try:
        I = I / np.linalg.norm(I)
    except:
        return np.array([0, 0])
    return I

def obliqueCollision(p1, p2):
    u1 = p1.getVel().copy()
    u2 = p2.getVel().copy()
    m1 = p1.getMass()
    m2 = p2.getMass()
    I = getLineOfCentres(p1.getPos(), p2.getPos())
    u1i = np.dot(u1, I)
    u2i = np.dot(u2, I)
    mT = m1 + m2
    totalInitialMomentum = (u1i * m1) + (u2i * m2)
    speedOfApproach = u1i - u2i

    v1i = (totalInitialMomentum - (m2 * e * speedOfApproach)) / mT
    v2i = (totalInitialMomentum + (m1 * e * speedOfApproach)) / mT

    u1j = u1 - (u1i * I)
    u2j = u2 - (u2i * I)

    v1 = (v1i * I) + u1j
    v2 = (v2i * I) + u2j

    return v1, v2


def floorCollision(p1):
    v = p1.getVelY().copy()
    v*=-1
    v *= p1.getFloorCoefficient()
    p1.changeVelY(v)

def wallCollision(p1):
    v = p1.getVelX().copy()
    v *= -1
    v *= p1.getFloorCoefficient()
    p1.changeVelX(v)

def calculateForces(particle1):
    #for particle2 in particles:
    #    if particle2.getID() != particle1.getID():
    #        r1 = particle1.getRadius()
    #        r2 = particle2.getRadius()
    #        if findDistance(particle1.getPos(), particle2.getPos()) <= (r1 + r2 + 3):
    #            v1, v2 = obliqueCollision(particle1, particle2)
    #            particle1.changeVel(v1)
    #            particle2.changeVel(v2)
    for particle2 in particles:
        if particle2.getID() <= particle1.getID():
            continue
        r1 = particle1.getRadius()
        r2 = particle2.getRadius()
        d = findDistance(particle1.getPos(), particle2.getPos())
        
        if d < (r1 + r2 + collisionLeaniance):
            v1, v2 = obliqueCollision(particle1, particle2)
            particle1.changeVel(v1)
            particle2.changeVel(v2)

            I = getLineOfCentres(particle1.getPos(), particle2.getPos())
            overlap = (r1 + r2) - d
            if I.all() != 0:
                particle1.changePos(particle1.getPos() - (I * (overlap / 2)) + collisionLeaniance / 2)
                particle2.changePos(particle2.getPos() + (I * (overlap / 2)) + collisionLeaniance / 2)

            else:
                particle1.changePos(particle1.getPos() - [r1, 0])
                particle2.changePos(particle2.getPos() + [r2, 0])
    
    pos = particle1.getPos()
    if pos[1] > HEIGHT - (particle1.getRadius()):
        floorCollision(particle1)
        #particle1.updateFloorCoefficient()
        particle1.changePosY(particle1.getY() - (particle1.getY() - HEIGHT + particle1.getRadius()))

    if pos[0] > WIDTH - (particle1.getRadius()):
        wallCollision(particle1)
        particle1.changePosX(particle1.getX() - (particle1.getX() - WIDTH + particle1.getRadius()))
    elif pos[0] < particle1.getRadius():
        wallCollision(particle1)
        particle1.changePosX(particle1.getX() + (0 - particle1.getX() + particle1.getRadius()))


    newPos = pos + (particle1.getVel() * (1 / fps))
    particle1.changePos(newPos)
    particle1.applyGravity()


#Creating the particle claass
class particle:
    _ID = 0
    def __init__(self, initialPos, radius, mass):
        #Initial pos is expected to be a tuple with 2 elements.
        self._mass = mass
        self._x = initialPos[0]
        self._y = initialPos[1]
        self._pos = [self._x, self._y]
        self._pos = np.array(self._pos)
        self._ID = particle._ID
        particle._ID += 1
        
        self._radius = radius
        self._collisionHandled = False

        self.floorCoefficient = eFloor

        self._velX = 0
        self._velY = 0
        self._vel = np.array([self._velX, self._velY])

    def getFloorCoefficient(self):
        return self.floorCoefficient
    
    def updateFloorCoefficient(self):
        if self.floorCoefficient > 0.1:
            self.floorCoefficient -= 0.1

    def getCollisionHandled(self):
        return self._collisionHandled
    
    def changeCollisionHandled(self):
        self._collisionHandled = not self._collisionHandled

    def getID(self):
        return self._ID

    def getMass(self):
        return self._mass

    def getRadius(self):
        return self._radius

    def setPos(self):
        self._pos[0] = self._x
        self._pos[1] = self._y

    def getPos(self):
        return self._pos
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def getVelX(self):
        return self._vel[0]
    
    def getVelY(self):
        return self._vel[1]
    
    def getVel(self):
        return self._vel
    
    def setVel(self):
        self._vel[0] = self._velX
        self._vel[1] = self._velY

    def changeVel(self, vel):
        self._velX = vel[0]
        self._velY = vel[1]
        self.setVel()

    def changeVelY(self, newVelY):
        self._vel[1] = newVelY

    def changeVelX(self, newVelX):
        self._vel[0] = newVelX

    def adjustVelY(self):
        self._vel[1] *= -1

    def applyGravity(self):
        self._vel[1] += (g * (1 / fps))

    def changePos(self, newPos):
        self._pos[0] = newPos[0]
        self._pos[1] = newPos[1]

    def changePosY(self, newY):
        self._pos[1] = newY

    def changePosX(self, newX):
        self._pos[0] = newX

    def getSpeed(self):
        mag = np.linalg.norm(self._vel)
        return mag


