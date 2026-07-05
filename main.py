import pygame

#Configuration settings, WIDTH and HEIGHT are the width and height of the GUI
WIDTH = 600
HEIGHT = 600
running = True
fps = 60

#Creating the necessary pygame objects, screen which is the object to handle the GUI and clock to handle timings and framerate.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#The main loop of the program, all necessary function calls and rendering will take place here.
def run():
    while running:
        #Redraw the background to clear old images
        screen.fill("black")

        #Pygame main event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        #Rendering and rendering function calls go here:
        pygame.draw.circle(screen, "red", (WIDTH/2, HEIGHT/2), 20)

        pygame.display.flip()

        #Controlling the pygame clock and finding the fps
        trueFps = round(clock.get_fps())
        clock.tick(fps)
        pygame.display.set_caption(f"Newtonian Physics Simulation | fps: {trueFps}")


run()