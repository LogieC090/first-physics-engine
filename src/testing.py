import numpy as np

def getLineOfCentres(pos1, pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    
    I = np.array([dx, dy])
    I = I / np.linalg.norm(I)

    return I



print(getLineOfCentres([3, 4], [4, 3]))



def returnStuff():
    a = 1
    b = 2
    return a, b


x, y = returnStuff()

print(x)
print(y)


x = True
print(x)
print(not x)