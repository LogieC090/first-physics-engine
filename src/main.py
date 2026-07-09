import pygame
import physics

pygame.init()

#Configuration settings, WIDTH and HEIGHT are the width and height of the GUI
with open("src\data.txt", "r") as file:
    data = file.readlines()

WIDTH = int(data[0])
HEIGHT = int(data[1])

running = True
fps = int(data[2])

#Creating the necessary pygame objects, screen which is the object to handle the GUI and clock to handle timings and framerate.
pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

radius = 10
particleSurf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
pygame.draw.circle(particleSurf, 'red', (radius, radius), radius)


#The main loop of the program, all necessary function calls and rendering will take place here.
def run():
    while running:
        #Redraw the background to clear old images
        screen.fill("dark grey")

        #Track the mouse and create a pygame rect so that it can interact with other pygame rects.
        mousePos = pygame.mouse.get_pos()
        mouseRect = pygame.rect.Rect(mousePos[0], mousePos[1], 2, 2)

        #Pygame main event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                physics.particles.append(physics.particle((mousePos[0], mousePos[1]), radius, 5))

    
        #Rendering and rendering function calls go here:
        for particle in physics.particles:
            physics.calculateForces(particle)
            screen.blit(particleSurf, (particle.getPos()[0] - radius, particle.getPos()[1] - radius))

        pygame.display.flip()

        #Controlling the pygame clock and finding the fps
        trueFps = round(clock.get_fps())
        clock.tick(fps)
        pygame.display.set_caption(f"Newtonian Physics Simulation | fps: {trueFps}")


run()