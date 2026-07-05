particles = []
springs = []

def calculateForces():
    for particle in particles:
        pass







#Creating the particle claass
class particle:
    def __init__(self, initialPos, radius):
        #Initial pos is expected to be a tuple with 2 elements.
        self.x = initialPos[0]
        self.y = initialPos[1]
        
        self.radius = radius

        self.velX = 0
        self.velY = 0


